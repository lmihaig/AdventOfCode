const WIDTH: usize = 1000;
const HEIGHT: usize = 200;

#[derive(Clone, Copy)]
enum Content {
    Air,
    Rock,
    Sand,
}
struct Grid {
    grid: [Content; WIDTH * HEIGHT],
    floor: usize,
}

impl Grid {
    pub fn new(input: &str) -> Self {
        let mut grid = [Content::Air; WIDTH * HEIGHT];
        let mut floor = 0;
        let lines = input.lines();
        for line in lines {
            let mut iter = line.split(" -> ").map(parse_point);
            let mut from = iter.next().unwrap();
            for to in iter {
                if from.0 == to.0 {
                    let min_y = from.1.min(to.1);
                    let max_y = from.1.max(to.1);
                    let x = to.0;
                    if max_y > floor {
                        floor = max_y;
                    }
                    for y in min_y..=max_y {
                        grid[WIDTH * y + x] = Content::Rock;
                    }
                } else {
                    let min_x = from.0.min(to.0);
                    let max_x = from.0.max(to.0);
                    let y = to.1;
                    if y > floor {
                        floor = y;
                    }
                    let start = y * WIDTH + min_x;
                    let end = y * WIDTH + max_x;
                    grid[start..=end].fill(Content::Rock);
                }
                from = to;
            }
        }
        floor += 2;
        Grid { grid, floor }
    }

    pub fn drop(&mut self) -> usize {
        let mut done = false;
        let mut total_sand = 0;
        loop {
            let mut tile: (usize, usize) = (500, 0);

            loop {
                if tile.1 >= self.floor - 1 {
                    done = true;
                    break;
                }

                if let Content::Air = self.get(tile.0, tile.1 + 1) {
                    tile = (tile.0, tile.1 + 1);
                    continue;
                }

                if let Content::Air = self.get(tile.0 - 1, tile.1 + 1) {
                    tile = (tile.0 - 1, tile.1 + 1);
                    continue;
                }

                if let Content::Air = self.get(tile.0 + 1, tile.1 + 1) {
                    tile = (tile.0 + 1, tile.1 + 1);
                    continue;
                }

                *self.get(tile.0, tile.1) = Content::Sand;
                total_sand += 1;
                break;
            }

            if done {
                break;
            }
        }
        total_sand
    }

    pub fn sweep(&mut self) -> usize {
        let mut sum = 1;
        let start_x = 500;
        *self.get(start_x, 0) = Content::Sand;
        for y in 0..self.floor - 1 {
            for x in 0..=1000 {
                if let Content::Sand = self.get(x, y) {
                    let tile = self.get(x - 1, y + 1);
                    if let Content::Air = tile {
                        *tile = Content::Sand;
                        sum += 1;
                    }
                    let tile = self.get(x, y + 1);
                    if let Content::Air = tile {
                        *tile = Content::Sand;
                        sum += 1;
                    }
                    let tile = self.get(x + 1, y + 1);
                    if let Content::Air = tile {
                        *tile = Content::Sand;
                        sum += 1;
                    }
                }
            }
        }
        sum
    }

    fn get(&mut self, col: usize, row: usize) -> &mut Content {
        &mut self.grid[WIDTH * row + col]
    }
}

fn parse_point(coord: &str) -> (usize, usize) {
    let (first, second) = coord.split_once(',').unwrap();
    (first.parse().unwrap(), second.parse().unwrap())
}

pub fn part1(input: String) -> usize {
    let mut grid = Grid::new(&input);
    grid.drop()
}

pub fn part2(input: String) -> usize {
    let mut grid = Grid::new(&input);
    grid.sweep()
}
