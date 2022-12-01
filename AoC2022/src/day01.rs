pub fn part1(input: String) -> usize {
    let mut ans = input
        .split("\n\n")
        .map(|x| {
            x.lines()
                .map(|l| l.parse::<usize>().unwrap())
                .sum::<usize>()
        })
        .collect::<Vec<_>>();

    ans.sort_by(|a, b| b.cmp(a));

    return ans[0];
}

pub fn part2(input: String) -> usize {
    let mut ans = input
        .split("\n\n")
        .map(|x| {
            x.lines()
                .map(|l| l.parse::<usize>().unwrap())
                .sum::<usize>()
        })
        .collect::<Vec<_>>();

    ans.sort_by(|a, b| b.cmp(a));

    return ans[0..3].iter().sum::<usize>();
}
