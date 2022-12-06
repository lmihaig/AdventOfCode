use itertools::Itertools;
use scan_fmt::scan_fmt;

use std::collections::VecDeque;

pub struct Instruction {
    num: usize,
    source: usize,
    destination: usize,
}

pub fn parse(input: &str) -> (Vec<VecDeque<char>>, impl Iterator<Item = Instruction> + '_) {
    let (crates, instructions) = input.split("\n\n").into_iter().collect_tuple().unwrap();

    let crates = crates
        .lines()
        .flat_map(|line| {
            line.chars()
                .skip(1)
                .step_by(4)
                .enumerate()
                .filter(|(_, c)| c.is_alphabetic())
        })
        .into_grouping_map()
        .collect::<VecDeque<char>>();

    let crates = crates
        .into_iter()
        .sorted_by_key(|(i, _)| *i)
        .map(|(_, stack)| stack)
        .collect();

    let instructions = instructions
        .lines()
        .filter_map(|line| scan_fmt!(line, "move {d} from {d} to {d}", usize, usize, usize).ok())
        .map(|(num, source, destination)| Instruction {
            num,
            source,
            destination,
        });

    return (crates, instructions);
}

pub fn part1(input: String) -> String {
    let (mut crates, instructions) = parse(&input);
    for inst in instructions {
        for _ in 0..inst.num {
            let item = crates[inst.source - 1].pop_front().unwrap();
            crates[inst.destination - 1].push_front(item);
        }
    }

    crates
        .into_iter()
        .filter_map(|mut x| x.pop_front())
        .collect::<String>()
}

pub fn part2(input: String) -> String {
    let (mut crates, instructions) = parse(&input);
    let mut buffer = VecDeque::new();
    for inst in instructions {
        for _ in 0..inst.num {
            let item = crates[inst.source - 1].pop_front().unwrap();
            buffer.push_back(item);
        }
        for _ in 0..inst.num {
            let item = buffer.pop_back().unwrap();
            crates[inst.destination - 1].push_front(item);
        }
    }

    crates
        .into_iter()
        .filter_map(|mut x| x.pop_front())
        .collect::<String>()
}
