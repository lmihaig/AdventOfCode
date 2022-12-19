use itertools::Itertools;
use serde::Deserialize;
use std::cmp::Ordering;

#[derive(Debug, Clone, Eq, Deserialize)]
#[serde(untagged)]
enum Packet {
    Term(u8),
    Nest(Vec<Self>),
}

impl Packet {
    pub fn as_slice(&self) -> &[Self] {
        if let Self::Nest(list) = self {
            list.as_slice()
        } else {
            std::slice::from_ref(self)
        }
    }
}

impl Ord for Packet {
    fn cmp(&self, other: &Self) -> Ordering {
        if let (Self::Term(a), Self::Term(b)) = (self, other) {
            a.cmp(b)
        } else {
            self.as_slice().cmp(other.as_slice())
        }
    }
}

impl PartialOrd for Packet {
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
        Some(self.cmp(other))
    }
}

impl PartialEq for Packet {
    fn eq(&self, rhs: &Self) -> bool {
        self.cmp(rhs).is_eq()
    }
}

pub fn part1(input: String) -> usize {
    let packets = input
        .lines()
        .filter(|l| !l.is_empty())
        .map(|line| serde_json::from_str::<Packet>(&line).unwrap());

    packets
        .enumerate()
        .tuple_windows()
        .step_by(2)
        .filter(|((_, x), (_, y))| x < y)
        .map(|((i, _), (_, _))| i / 2 + 1)
        .sum()
}

pub fn part2(input: String) -> usize {
    let mut packets: Vec<Packet> = input
        .lines()
        .filter(|l| !l.is_empty())
        .map(|line| serde_json::from_str::<Packet>(&line).unwrap())
        .collect();

    let packet_1: Packet = serde_json::from_str("[[2]]").unwrap();
    let packet_2: Packet = serde_json::from_str("[[6]]").unwrap();
    packets.push(packet_1.clone());
    packets.push(packet_2.clone());

    packets.sort();

    let id_packet_1 = packets.binary_search(&packet_1).unwrap() + 1;
    let id_packet_2 = packets.binary_search(&packet_2).unwrap() + 1;

    id_packet_1 * id_packet_2
}
