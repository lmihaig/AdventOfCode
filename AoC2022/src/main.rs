#![allow(dead_code)]
mod day01;
mod day02;
mod day03;
mod day04;
mod day05;
mod day06;

fn read_input(day: usize) -> String {
    std::fs::read_to_string(format!("data/day{:0>2}.txt", day)).unwrap()
}
fn main() {
    println!("Part1: {}", day06::part1(read_input(6)));
    println!("Part2: {}", day06::part2(read_input(6)));
}
