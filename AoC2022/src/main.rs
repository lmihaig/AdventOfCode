#![allow(dead_code)]
mod day01;
mod day02;
mod day03;
mod day04;

fn read_input(day: usize) -> String {
    std::fs::read_to_string(format!("data/day{:0>2}.txt", day)).unwrap()
}
fn main() {
    println!("Part1: {}", day04::part1(read_input(4)));
    println!("Part2: {}", day04::part2(read_input(4)));
}
