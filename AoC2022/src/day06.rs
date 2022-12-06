use itertools::Itertools;

pub fn solve(input: String, WINDOW_SIZE: usize) -> usize {
    let input = input.trim().chars().collect_vec();
    return input
        .windows(WINDOW_SIZE)
        .find_position(|window| window.into_iter().all_unique())
        .map(|(i, _)| i + WINDOW_SIZE)
        .unwrap();
}

pub fn part1(input: String) -> usize {
    return solve(input, 4);
}

pub fn part2(input: String) -> usize {
    return solve(input, 14);
}
