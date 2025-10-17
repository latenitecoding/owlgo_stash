const std = @import("std");
const stdin = std.fs.File.stdin();
const stdout = std.fs.File.stdout();

pub fn main() !void {
    var r = Stdin.init(1024);
    var w = Stdout.init(1024);

    const n = try r.next(usize);
    const m = try r.last(usize);

    try w.print("{} {}\n", .{n, m});
}

// ==========================================
// HELPERS
// ==========================================

const Stdin = struct {
    reader: *std.Io.Reader,

    pub inline fn init(comptime N: usize) Stdin {
        var buf: [N]u8 = undefined;
        var reader = stdin.readerStreaming(&buf);
        return Stdin {
            .reader = &reader.interface,
        };
    }

    pub fn last(self: *Stdin, comptime T: type) !T {
        const token = try self.reader.takeDelimiterExclusive('\n');
        return try Stdin.parse(T, token);
    }

    pub fn next(self: *Stdin, comptime T: type) !T {
        const token = try self.reader.takeDelimiterExclusive(' ');
        return try Stdin.parse(T, token);
    }

    pub fn nextLine(self: *Stdin) ![]u8 {
        return try self.reader.takeDelimiterExclusive('\n');
    }

    pub fn nextList(self: *Stdin, comptime T: type, list: []T) !usize {
        const line = try self.nextLine();
        var it = std.mem.splitScalar(u8, line, ' ');

        var i: usize = 0;
        while (it.next()) |token| : (i += 1) {
            list[i] = try Stdin.parse(T, token);
        }

        return i;
    }

    fn parse(comptime T: type, token: []const u8) !T {
        if (T == i8 or T == i16 or T == i32 or T == i64 or T == i128 or T == isize) {
            return try std.fmt.parseInt(T, token, 10);
        } else if (T == u16 or T == u32 or T == u64 or T == u128 or T == usize) {
            return try std.fmt.parseInt(T, token, 10);
        } else if (T == f16 or T == f32 or T == f64 or T == f80 or T == f128) {
            return try std.fmt.parseFloat(T, token);
        } else if (T == bool) {
            return std.mem.eql(u8, token, "true");
        } else if (T == u8) {
            return token[0];
        } else {
            return token;
        }
    }
};

const Stdout = struct {
    writer: *std.Io.Writer,

    pub inline fn init(comptime N: usize) @This() {
        var buf: [N]u8 = undefined;
        var writer = stdout.writerStreaming(&buf);
        return .{
            .writer = &writer.interface,
        };
    }

    pub fn print(self: *@This(), comptime fmt: []const u8, args: anytype) !void {
        try self.writer.print(fmt, args);
        try self.writer.flush();
    }

    pub fn printList(self: *@This(), comptime T: type, comptime fmt: []const u8, args: []const T) !void {
        try self.writer.print(fmt, .{args[0]});
        for (1..args.len) |i| {
            try self.writer.writeByte(' ');
            try self.writer.print(fmt, .{args[i]});
        }
        try self.writer.print("\n", .{});
        try self.writer.flush();
    }
};
