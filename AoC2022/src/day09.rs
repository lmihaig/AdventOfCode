fn parse(input: String) -> Vec<((isize, isize), isize)> {
    input
        .lines()
        .flat_map(|line| {
            line.split_once(" ")
                .and_then(|(d, m)| match (d, m.parse::<isize>().unwrap()) {
                    ("U", m) => Some(((0, 1), m)),
                    ("D", m) => Some(((0, -1), m)),
                    ("L", m) => Some(((-1, 0), m)),
                    ("R", m) => Some(((1, 0), m)),
                    _ => panic!(),
                })
        })
        .collect()
}

fn solve(input: Vec<((isize, isize), isize)>, knots: usize) -> usize {
    std::iter::once((vec![(0, 0); knots + 1], input))
        .fold(
            std::collections::HashSet::from([(0, 0)]),
            |mut seen, (mut pos, motions)| {
                for ((dx, dy), steps) in motions {
                    (0..steps).for_each(|_| {
                        (0..3).for_each(|i| match i {
                            0 => pos[0] = (pos[0].0 + dx, pos[0].1 + dy),
                            1 => (1..pos.len()).for_each(|i| {
                                std::iter::once((pos[i - 1].0 - pos[i].0, pos[i - 1].1 - pos[i].1))
                                    .for_each(|(dx, dy)| {
                                        if dx.abs().max(dy.abs()) > 1 {
                                            pos[i] =
                                                (pos[i].0 + dx.signum(), pos[i].1 + dy.signum())
                                        }
                                    })
                            }),
                            _ => seen.extend(std::iter::once(pos[knots])),
                        })
                    })
                }

                seen
            },
        )
        .len()
}

pub fn part1(input: String) -> usize {
    let input = parse(input);
    solve(input, 1)
}

pub fn part2(input: String) -> usize {
    let input = parse(input);
    solve(input, 9)
}
