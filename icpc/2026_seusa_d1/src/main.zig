const std = @import("std");
const Io = std.Io;

pub fn main(init: std.process.Init) !void {
    var scanner: Scanner(1024) = .init(init.io);
    const n = try scanner.next(u32);

    const stdout: Printer(1024) = .init(init.io);
    try stdout.println("{}", .{n});
}

//==============================================================================
// HELPERS
//==============================================================================

pub fn Printer(comptime buffer_len: usize) type {
    return struct {
        buffer: [buffer_len]u8,
        writer: *Io.Writer,

        pub inline fn init(io: Io) @This() {
            var stdout_buffer: [buffer_len]u8 = undefined;
            var stdout_writer: Io.File.Writer = .init(.stdout(), io, &stdout_buffer);

            return .{
                .buffer = stdout_buffer,
                .writer = &stdout_writer.interface,
            };
        }

        pub fn print(self: *const @This(), comptime fmt: []const u8, args: anytype) !void {
            try self.writer.print(fmt, args);
            try self.writer.flush();
        }

        pub fn println(self: *const @This(), comptime fmt: []const u8, args: anytype) !void {
            try self.writer.print(fmt, args);
            try self.writer.print("\n", .{});
            try self.writer.flush();
        }
    };
}

pub fn Scanner(comptime buffer_len: usize) type {
    return struct {
        buffer: [buffer_len]u8,
        line: ?[]u8,
        reader: *Io.Reader,

        pub inline fn init(io: Io) @This() {
            var stdin_buffer: [buffer_len]u8 = undefined;
            var stdin_reader: Io.File.Reader = .init(.stdin(), io, &stdin_buffer);

            return .{
                .buffer = stdin_buffer,
                .line = null,
                .reader = &stdin_reader.interface,
            };
        }

        fn loadLine(self: *@This()) !void {
            if (self.line != null) {
                return;
            }

            self.line = try self.reader.takeDelimiterExclusive('\n');
            _ = try self.reader.take(1);
        }

        fn parse(comptime T: type, token: []u8) !T {
            if (T == i8 or T == i16 or T == i32 or T == i64 or T == i128 or T == isize) {
                return std.fmt.parseInt(T, token, 10);
            } else if (T == u16 or T == u32 or T == u64 or T == u128 or T == usize) {
                return std.fmt.parseInt(T, token, 10);
            } else if (T == f16 or T == f32 or T == f64 or T == f128) {
                return std.fmt.parseFloat(T, token);
            } else if (T == bool) {
                return std.mem.eql(u8, token, "true");
            } else if (T == u8) {
                return token[0];
            }
            return token;
        }

        pub fn next(self: *@This(), comptime T: type) !T {
            if (self.line == null) {
                try self.loadLine();
            }

            if (self.line) |line| {
                if (std.mem.findScalar(u8, line, ' ')) |pos| {
                    const token = line[0..pos];
                    self.line = line[(pos + 1)..];
                    return parse(T, token);
                }

                const token = line;
                self.line = null;
                return parse(T, token);
            }

            return error.EndOfStream;
        }

        pub fn nextLine(self: *@This()) ![]u8 {
            if (self.line) |line| {
                self.line = null;
                return line;
            }

            const line = self.reader.takeDelimiterExclusive('\n');
            _ = try self.reader.take(1);
            return line;
        }

        pub fn nextList(self: *@This(), comptime T: type, list: []T) !usize {
            const line = try self.nextLine();
            var it = std.mem.splitScalar(u8, line, ' ');

            var i: usize = 0;
            while (it.next()) |token| : (i += 1) {
                list[i] = try parse(T, token);
            }

            return i;
        }
    };
}
