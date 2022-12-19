use pathfinding::prelude::Grid;

fn parse(input: String) -> Vec<i32> {
    let mut x = 1;
    input.lines().fold(vec![], |acc, s| {
        if let Some(v) = s.strip_prefix("addx ") {
            let r = vec![x, x];
            x += v.parse::<i32>().unwrap();
            acc.into_iter().chain(r).collect()
        } else {
            acc.into_iter().chain(vec![x]).collect()
        }
    })
}

pub fn part1(input: String) -> i32 {
    let input = parse(input);
    input
        .into_iter()
        .enumerate()
        .skip(19)
        .step_by(40)
        .map(|(opcode, val)| val * (opcode + 1) as i32)
        .sum()
}

pub fn part2(input: String) -> String {
    let input = parse(input);

    let input = input
        .into_iter()
        .enumerate()
        .flat_map(|(i, x)| (x.abs_diff(i as i32 % 40) <= 1).then_some((i % 40, i / 40)))
        .collect::<Grid>();
    format!("\n{input:#?}")
}
