use itertools::Itertools;

pub fn priority(item: u8) -> u32 {
    match item {
        b'a'..=b'z' => item as u32 - 96,
        b'A'..=b'Z' => item as u32 - 38,
        _ => 0,
    }
}

pub fn same_chars(l: &[u8], r: &[u8]) -> Vec<u8> {
    l.iter().copied().filter(|c| r.contains(c)).collect()
}

pub fn part1(input: String) -> u32 {
    let sum = input
        .lines()
        .map(|line| line.split_at(line.len() / 2))
        .map(|(l, r)| same_chars(l.as_bytes(), r.as_bytes())) // this is bad
        .map(|c| priority(c[0]))
        .sum::<u32>();
    return sum;
}

pub fn part2(input: String) -> u32 {
    let sum = input
        .lines()
        .tuples::<(_, _, _)>()
        .map(|(a, b, c)| same_chars(a.as_bytes(), &same_chars(b.as_bytes(), c.as_bytes())))
        .map(|c| priority(c[0]))
        .sum::<u32>();

    return sum;
}
