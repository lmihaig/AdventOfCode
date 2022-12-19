use std::collections::VecDeque;

fn find_indices(vec: &Vec<Vec<u8>>, target: u8) -> (usize, usize) {
    for (i, inner_vec) in vec.iter().enumerate() {
        for (j, &x) in inner_vec.iter().enumerate() {
            if x == target {
                return (i, j);
            }
        }
    }
    (0, 0)
}

fn bfs(grid: &Vec<Vec<u8>>, start: (usize, usize), end: (usize, usize), part: u8) -> usize {
    let mut visited = vec![vec![false; grid[0].len()]; grid.len()];
    let mut queue = VecDeque::from_iter([(start.0, start.1, 0)].into_iter());

    while let Some((x, y, len)) = queue.pop_front() {
        if part == 2 && grid[x][y] == b'a' {
            return len;
        }
        if (x, y) == end {
            return len;
        }
        for (dx, dy) in [(0, -1), (-1, 0), (0, 1), (1, 0)] {
            let (nx, ny) = ((x as isize + dx) as usize, (y as isize + dy) as usize);
            let Some(&square) = grid.get(nx).and_then(|row| row.get(ny)) else { continue };
            if grid[x][y] - 1 <= square && !visited[nx][ny] {
                visited[nx][ny] = true;
                queue.push_back((nx, ny, len + 1));
            }
        }
    }
    0
}
pub fn part1(input: String) -> usize {
    let mut grid = input
        .lines()
        .map(|l| l.as_bytes().iter().copied().collect::<Vec<_>>())
        .collect::<Vec<_>>();
    let (start_x, start_y) = find_indices(&grid, b'S');
    let (end_x, end_y) = find_indices(&grid, b'E');
    grid[start_x][start_y] = b'a';
    grid[end_x][end_y] = b'z';

    bfs(&grid, (end_x, end_y), (start_x, start_y), 1)
}

pub fn part2(input: String) -> usize {
    let mut grid = input
        .lines()
        .map(|l| l.as_bytes().iter().copied().collect::<Vec<_>>())
        .collect::<Vec<_>>();
    let (start_x, start_y) = find_indices(&grid, b'S');
    let (end_x, end_y) = find_indices(&grid, b'E');
    grid[start_x][start_y] = b'a';
    grid[end_x][end_y] = b'z';

    let (start_x, start_y) = find_indices(&grid, b'a');
    bfs(&grid, (end_x, end_y), (start_x, start_y), 2)
}
