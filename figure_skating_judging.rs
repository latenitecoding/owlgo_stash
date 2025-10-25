use std::fmt::Debug;
use std::io::{self, BufRead};
use std::str::FromStr;

fn main() {
    let n = next_int::<usize>();
    let k = last_int::<usize>();

    let mut diffs = next_list::<u32>(n);
    diffs.sort_unstable();

    let mut sum_to_square: u64 = 0;
    let mut sum_squares: u64 = 0;

    for x in diffs.iter().take(k) {
        let square_x = (*x as u64) * (*x as u64);

        sum_to_square += *x as u64;
        sum_squares += square_x;
    }

    let mut badness = as_badness(sum_squares, sum_to_square, k);

    for (y, x) in diffs.iter().skip(k).zip(diffs.iter()){
        let square_x = (*x as u64) * (*x as u64);
        let square_y = (*y as u64) * (*y as u64);

        sum_to_square -= *x as u64;
        sum_squares -= square_x;

        sum_to_square += *y as u64;
        sum_squares += square_y;

        let local_badness = as_badness(sum_squares, sum_to_square, k);
        if local_badness < badness {
            badness = local_badness;
        }
    }

    println!("{:.6}", badness);
}

fn as_badness(sum_squares: u64, sum_to_square: u64, k: usize) -> f64 {
    let mean = (sum_to_square as f64) / (k as f64);
    (sum_squares as f64) - (2f64 * mean * sum_to_square as f64) + (k as f64 * mean * mean)
}

//==========================================================
// Helpers
//==========================================================

#[allow(dead_code)]
fn last_float<T: Real>() -> T
where <T as FromStr>::Err: Debug
{
    let mut buffer = String::new();
    io::stdin().read_line(&mut buffer).expect("%f\n");

    buffer.trim().parse::<T>().expect("parseable as float")
}

#[allow(dead_code)]
fn last_int<T: Num>() -> T
where <T as FromStr>::Err: Debug
{
    let mut buffer = String::new();
    io::stdin().read_line(&mut buffer).expect("%d\n");

    buffer.trim().parse::<T>().expect("parseable as int")
}

#[allow(dead_code)]
fn next() -> String {
    let mut buffer: Vec<u8> = Vec::new();

    io::stdin().lock().read_until(b' ', &mut buffer).expect("contains space");

    String::from_utf8(buffer).expect("parseable as utf8")
}

#[allow(dead_code)]
fn next_float<T: Num>() -> T
where <T as FromStr>::Err: Debug
{
    next().trim().parse::<T>().expect("parseable as float")
}

#[allow(dead_code)]
fn next_int<T: Num>() -> T
where <T as FromStr>::Err: Debug
{
    next().trim().parse::<T>().expect("parseable as int")
}

#[allow(dead_code)]
fn next_line() -> String {
    let mut buffer = String::new();
    io::stdin().read_line(&mut buffer).expect("%s\n");

    buffer
}

#[allow(dead_code)]
fn next_list<T: Real>(n: usize) -> Vec<T>
where <T as FromStr>::Err: Debug {
    let mut vec: Vec<T> = Vec::new();

    while vec.len() < n {
        let mut buffer = String::new();
        io::stdin().read_line(&mut buffer).expect("%s\n");


        buffer
            .trim()
            .split(' ')
            .map(|s| s.parse::<T>().expect("parseable as any number type"))
            .for_each(|num| vec.push(num))
    }

    vec
}

#[allow(dead_code)]
fn next_tuple<T: Real>() -> (T, T)
where <T as FromStr>::Err: Debug {
    let mut buffer = String::new();
    io::stdin().read_line(&mut buffer).expect("%s\n");

    let mut tuple = buffer
        .trim()
        .split(' ')
        .map(|s| s.parse::<T>().expect("parseable as any number type"));

    (
        tuple.next().expect("(?,)"),
        tuple.next().expect("(,?)"),
    )
}

//==========================================================
// Type System
//==========================================================

#[allow(dead_code)]
trait Real: Sized + FromStr + Debug {}
#[allow(dead_code)]
trait Num: Real {}
#[allow(dead_code)]
trait Int: Num {}
#[allow(dead_code)]
trait Nat: Num {}

macro_rules! is_int {
    ($alias:ty) => {
        impl Real for $alias {}
        impl Num for $alias {}
        impl Int for $alias {}
    }
}
macro_rules! is_nat {
    ($alias:ty) => {
        impl Real for $alias {}
        impl Num for $alias {}
        impl Nat for $alias {}
    }
}

macro_rules! is_real {
    ($alias:ty) => {
        impl Real for $alias {}
    }
}

is_int!(i16);
is_int!(i32);
is_int!(i64);
is_int!(i128);
is_int!(isize);

is_nat!(u16);
is_nat!(u32);
is_nat!(u64);
is_nat!(u128);
is_nat!(usize);

is_real!(f32);
is_real!(f64);

//==========================================================
