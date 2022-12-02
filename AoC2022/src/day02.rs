use core::panic;

const WIN: u32 = 6;
const DRAW: u32 = 3;
const LOSE: u32 = 0;

const ROCK: u32 = 1;
const PAPER: u32 = 2;
const SCISSORS: u32 = 3;

pub fn part1(input: String) -> u32 {
    let mut score = 0;

    for line in input.lines() {
        let mut l = line.split_whitespace();

        let opponent = l.next().unwrap();
        let me = l.next().unwrap();

        score += match me {
            "X" => {
                ROCK + match opponent {
                    "A" => DRAW,
                    "B" => LOSE,
                    _ => WIN,
                }
            }
            "Y" => {
                PAPER
                    + match opponent {
                        "A" => WIN,
                        "B" => DRAW,
                        _ => LOSE,
                    }
            }
            "Z" => {
                SCISSORS
                    + match opponent {
                        "A" => LOSE,
                        "B" => WIN,
                        _ => DRAW,
                    }
            }
            _ => panic!(),
        }
    }
    return score;
}

pub fn part2(input: String) -> u32 {
    let mut score = 0;

    for line in input.lines() {
        let mut l = line.split_whitespace();

        let opponent = l.next().unwrap();
        let condition = l.next().unwrap();

        score += match opponent {
            "A" => match condition {
                "Z" => WIN + PAPER,
                "Y" => DRAW + ROCK,
                _ => LOSE + SCISSORS,
            },
            "B" => match condition {
                "Z" => WIN + SCISSORS,
                "Y" => DRAW + PAPER,
                _ => LOSE + ROCK,
            },
            "C" => match condition {
                "Z" => WIN + ROCK,
                "Y" => DRAW + SCISSORS,
                _ => LOSE + PAPER,
            },
            _ => panic!(),
        }
    }
    return score;
}
