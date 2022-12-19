use itertools::{izip, Itertools};

fn determine_visibility(grid: &Vec<Vec<u8>>, width: usize, height: usize) -> Vec<Vec<(u64, bool)>> {
    let mut result = vec![vec![(1, false); grid.len()]; grid.len()];

    for i in 0..height {
        for j in 0..width {
            let mut scenic_score = 0;
            let mut found = false;
            for dy in (0..i).rev() {
                scenic_score += 1;
                if grid[i][j] <= grid[dy][j] {
                    found = true;
                    result[i][j] = (scenic_score.max(1), false);
                    break;
                }
            }
            if !found {
                result[i][j] = (scenic_score.max(1), true)
            }
        }
    }

    return result;
}

fn transpose<T>(v: Vec<Vec<T>>) -> Vec<Vec<T>> {
    assert!(!v.is_empty());
    let len = v[0].len();
    let mut iters: Vec<_> = v.into_iter().map(|n| n.into_iter()).collect();
    (0..len)
        .map(|_| {
            iters
                .iter_mut()
                .map(|n| n.next().unwrap())
                .collect::<Vec<T>>()
        })
        .collect()
}

// Helper function to reverse the rows of a matrix
fn reverse_rows<T: Clone>(matrix: &Vec<Vec<T>>) -> Vec<Vec<T>> {
    let mut reversed = matrix.clone();
    for row in reversed.iter_mut() {
        row.reverse();
    }
    reversed
}

// Implement rot90 using the helper functions
fn rot90<T: Clone>(matrix: &mut Vec<Vec<T>>) {
    let transposed = transpose(matrix.to_vec());
    let reversed = reverse_rows(&transposed);
    *matrix = reversed;
}

fn transform(vec: Vec<u8>, n: usize, m: usize) -> Vec<Vec<u8>> {
    let mut transformed = vec![vec![0; m]; m];

    for i in 0..n {
        for j in 0..m {
            transformed[i][j] = vec[i * m + j] - b'0';
        }
    }

    transformed
}

pub fn solve(
    input: String,
) -> (
    Vec<Vec<(u64, bool)>>,
    Vec<Vec<(u64, bool)>>,
    Vec<Vec<(u64, bool)>>,
    Vec<Vec<(u64, bool)>>,
) {
    let twod_arr: Vec<u8> = input.lines().flat_map(|l| l.trim().bytes()).collect_vec();
    let width = input.lines().next().unwrap().trim().len();
    let height = twod_arr.len() / width;

    let mut grid = transform(twod_arr, height, width);

    let mut top = determine_visibility(&grid, width, height);
    rot90(&mut top);
    rot90(&mut top);
    rot90(&mut top);

    rot90(&mut grid);

    let mut left = determine_visibility(&grid, width, height);
    rot90(&mut left);
    rot90(&mut left);
    rot90(&mut grid);

    let mut bottom = determine_visibility(&grid, width, height);
    rot90(&mut bottom);
    rot90(&mut grid);

    let right = determine_visibility(&grid, width, height);

    return (top, bottom, left, right);
}

pub fn part1(input: String) -> usize {
    let (top, bottom, left, right) = solve(input);
    let c = izip!(
        top.into_iter().flatten(),
        bottom.into_iter().flatten(),
        left.into_iter().flatten(),
        right.into_iter().flatten()
    )
    .filter(|(t, b, l, r)| t.1 | b.1 | l.1 | r.1)
    .count();
    return c;
}

pub fn part2(input: String) -> usize {
    let (top, bottom, left, right) = solve(input);
    let c = izip!(
        top.into_iter().flatten(),
        bottom.into_iter().flatten(),
        left.into_iter().flatten(),
        right.into_iter().flatten()
    )
    .map(|(t, b, l, r)| t.0 * b.0 * l.0 * r.0)
    .max()
    .unwrap();
    return c as usize;
}
