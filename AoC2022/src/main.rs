#![allow(dead_code)]
mod day01;
mod day02;

fn read_input(day: usize) -> String {
    std::fs::read_to_string(format!("../data/day{:0>2}.txt", day)).unwrap()
}
fn main() {
    println!("Part1: {}", day02::part1(read_input(2)));
    println!("Part2: {}", day02::part2(read_input(2)));
}
