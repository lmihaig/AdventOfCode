#[derive(Debug, Clone)]
struct Monkey {
    items: Vec<usize>,
    operation: Operation,
    div: usize,
    true_monkey: usize,
    false_monkey: usize,
    inspections: usize,
}
#[derive(Debug, Clone, Copy)]
enum Operation {
    Add(usize),
    Multiply(usize),
    MultiplyOld,
}

impl Operation {
    fn execute(&self, x: usize) -> usize {
        match self {
            Operation::Add(x2) => x + x2,
            Operation::Multiply(x2) => x * x2,
            Operation::MultiplyOld => x * x,
        }
    }
}

fn solve(input: String) -> Vec<Monkey> {
    let mut monkeys: Vec<Monkey> = Vec::new();
    for monkey in input.split("\n\n") {
        let mut lines = monkey.lines().skip(1);

        let (_, items) = lines.next().unwrap().split_once(": ").unwrap();
        let items: Vec<usize> = items
            .split_terminator(", ")
            .filter_map(|s| s.parse().ok())
            .collect();

        let (_, operation) = lines.next().unwrap().split_once("= old ").unwrap();
        let (operator, operand) = operation.split_once(" ").unwrap();
        let op = match operand {
            "old" => Operation::MultiplyOld,
            x => match operator {
                "+" => Operation::Add(x.parse().ok().unwrap()),
                "*" => Operation::Multiply(x.parse().ok().unwrap()),
                _ => panic!(),
            },
        };

        let (_, div) = lines.next().unwrap().split_once("divisible by ").unwrap();
        let div: usize = div.parse().unwrap();

        let (_, true_monkey) = lines.next().unwrap().split_once("to monkey ").unwrap();
        let true_monkey = true_monkey.parse().unwrap();

        let (_, false_monkey) = lines.next().unwrap().split_once("to monkey ").unwrap();
        let false_monkey = false_monkey.parse().unwrap();

        let monkey = Monkey {
            items,
            operation: op,
            div,
            true_monkey,
            false_monkey,
            inspections: 0,
        };

        monkeys.push(monkey);
    }

    return monkeys;
}

pub fn part1(input: String) -> usize {
    let mut monkeys = solve(input);
    for _ in 0..20 {
        for id in 0..monkeys.len() {
            let items: Vec<usize> = monkeys[id].items.drain(..).collect();
            let monkey = monkeys[id].clone();
            for old in items {
                monkeys[id].inspections += 1;
                let new = monkey.operation.execute(old);
                let new = new / 3;
                let id = if new % monkey.div == 0 {
                    monkey.true_monkey
                } else {
                    monkey.false_monkey
                };

                let recv = &mut monkeys[id];
                recv.items.push(new);
            }
        }
    }

    monkeys.sort_by_key(|monkey| monkey.inspections);
    monkeys
        .iter()
        .cloned()
        .map(|monkey| monkey.inspections)
        .rev()
        .take(2)
        .product()
}

pub fn part2(input: String) -> usize {
    let mut monkeys = solve(input);
    let common_multiple: usize = monkeys.iter().map(|monkey| monkey.div).product();
    for _ in 0..10000 {
        for id in 0..monkeys.len() {
            let items: Vec<usize> = monkeys[id].items.drain(..).collect();
            let monkey = monkeys[id].clone();
            for old in items {
                monkeys[id].inspections += 1;
                let new = monkey.operation.execute(old);
                let new = new % common_multiple;
                let id = if new % monkey.div == 0 {
                    monkey.true_monkey
                } else {
                    monkey.false_monkey
                };

                let recv = &mut monkeys[id];
                recv.items.push(new);
            }
        }
    }

    monkeys.sort_by_key(|monkey| monkey.inspections);
    monkeys
        .iter()
        .cloned()
        .map(|monkey| monkey.inspections)
        .rev()
        .take(2)
        .product()
}
