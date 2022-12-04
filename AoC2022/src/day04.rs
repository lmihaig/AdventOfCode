use itertools::Itertools;

pub fn part1(input: String) -> usize {
    let c = input
        .lines()
        .map(|line| {
            line.split(['-', ','])
                .map(|v| v.parse::<u32>().unwrap())
                .collect_tuple::<(_, _, _, _)>()
                .unwrap()
        })
        .filter(|(a, b, c, d)| (a <= c && b >= d) || (c <= a && d >= b))
        .count();

    return c;
}

pub fn part2(input: String) -> usize {
    let c = input
        .lines()
        .map(|line| {
            line.split(['-', ','])
                .map(|v| v.parse::<u32>().unwrap())
                .collect_tuple::<(_, _, _, _)>()
                .unwrap()
        })
        .filter(|(a, b, c, d)| (a <= c && b >= c) || (c <= a && d >= a))
        .count();

    return c;
}
