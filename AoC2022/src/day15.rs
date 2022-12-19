use std::collections::HashSet;

use scan_fmt::scan_fmt;

#[derive(Debug, Clone, Copy)]
pub struct Sensor {
    coords: (isize, isize),
    beacon: (isize, isize),
    range: isize,
}

impl Sensor {
    pub fn new(input: &str) -> Self {
        input
            .lines()
            .filter_map(|line| {
                scan_fmt!(
                    line,
                    "Sensor at x={d}, y={d}: closest beacon is at x={d}, y={d}",
                    isize,
                    isize,
                    isize,
                    isize
                )
                .ok()
            })
            .map(|(x, y, x_beacon, y_beacon)| {
                (
                    (x, y),
                    (x_beacon, y_beacon),
                    (x - x_beacon).abs() + (y - y_beacon).abs(),
                )
            })
            .map(|((x, y), (x_beacon, y_beacon), range)| Sensor {
                coords: (x, y),
                beacon: (x_beacon, y_beacon),
                range: range,
            })
            .next()
            .unwrap()
    }

    fn can_contain_unseen_points(&self, min: (isize, isize), max: (isize, isize)) -> bool {
        let corners = [
            (min.0, min.1),
            (min.0, max.1),
            (max.0, min.1),
            (max.0, max.1),
        ];
        let largest_dist = corners
            .iter()
            .map(|corner| (corner.0 - self.coords.0).abs() + (corner.1 - self.coords.1).abs())
            .max()
            .unwrap();
        largest_dist > self.range
    }
}

pub fn num_impossible_beacon(sensors: Vec<Sensor>, row: isize) -> usize {
    let occupied_positions: HashSet<(isize, isize)> = sensors
        .iter()
        .flat_map(|sensor| [sensor.coords, sensor.beacon])
        .collect();

    let mut no_beacons: HashSet<(isize, isize)> = HashSet::new();

    let max_range = sensors.iter().map(|sensor| sensor.range).max().unwrap();

    let min_x = sensors
        .iter()
        .map(|sensor| sensor.coords.0.min(sensor.beacon.0))
        .min()
        .unwrap()
        - max_range;
    let max_x = sensors
        .iter()
        .map(|sensor| sensor.coords.0.max(sensor.beacon.0))
        .max()
        .unwrap()
        + max_range;

    for new_x in min_x..=max_x {
        let position = (new_x, row);
        if occupied_positions.contains(&position) {
            continue;
        }
        if sensors.iter().any(|sensor| {
            (sensor.coords.0 - position.0).abs() + (sensor.coords.1 - position.1).abs()
                <= sensor.range
        }) {
            no_beacons.insert((new_x, row));
        }
    }
    no_beacons.len()
}

fn find_unseen_point(
    sensors: Vec<Sensor>,
    min: (isize, isize),
    max: (isize, isize),
) -> (isize, isize) {
    let mut stack = vec![(min, max)];

    while let Some((min, max)) = stack.pop() {
        if min == max {
            if sensors.iter().all(|sensor| {
                !((sensor.coords.0 - min.0).abs() + (sensor.coords.1 - min.1).abs() <= sensor.range)
            }) {
                return min;
            }
        } else {
            let mid = ((min.0 + max.0) / 2, (min.1 + max.1) / 2);

            let quadrants = [
                (min, mid),
                ((mid.0 + 1, min.1), (max.0, mid.1)),
                ((min.0, mid.1 + 1), (mid.0, max.1)),
                ((mid.0 + 1, mid.1 + 1), max),
            ];

            for quadrant in quadrants.iter() {
                if quadrant.0 .0 > quadrant.1 .0 || quadrant.0 .1 > quadrant.1 .1 {
                    continue;
                }
                if sensors
                    .iter()
                    .all(|sensor| sensor.can_contain_unseen_points(quadrant.0, quadrant.1))
                {
                    stack.push(*quadrant);
                }
            }
        }
    }
    min
}

pub fn part1(input: String) -> usize {
    let sensors: Vec<Sensor> = input.lines().map(|line| Sensor::new(line)).collect();

    const Y: isize = 2_000_000;
    num_impossible_beacon(sensors, Y)
}

pub fn part2(input: String) -> isize {
    let sensors: Vec<Sensor> = input.lines().map(|line| Sensor::new(line)).collect();
    const MIN_XY: isize = 0;
    const MAX_XY: isize = 4_000_000;
    let min = (MIN_XY, MIN_XY);
    let max = (MAX_XY, MAX_XY);

    let found_position = find_unseen_point(sensors, min, max);

    found_position.0 * MAX_XY + found_position.1
}
