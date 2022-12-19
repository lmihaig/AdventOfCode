#![allow(dead_code)]
mod day01;
mod day02;
mod day03;
mod day04;
mod day05;
mod day06;
mod day07;
mod day08;
mod day09;
mod day10;
mod day11;
mod day12;
mod day13;
mod day14;
mod day15;
mod day16;
mod day17;
mod day18;
mod day19;
mod day20;
mod day21;
mod day22;
mod day23;
mod day24;
mod day25;

fn read_input(day: usize) -> String {
    std::fs::read_to_string(format!("data/day{:0>2}.txt", day)).unwrap()
}
fn main() {
    let day = 14;
    println!("Part1: {}", day14::part1(read_input(day)));
    println!("Part2: {}", day14::part2(read_input(day)));
}
