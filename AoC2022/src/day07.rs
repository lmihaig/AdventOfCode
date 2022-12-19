use id_tree::{Node, Tree};
use itertools::Itertools;
use std::path::PathBuf;

#[derive(Debug)]
pub struct FsEntry {
    path: PathBuf,
    size: usize,
}

pub fn dir_maps(input: String) -> Tree<FsEntry> {
    let mut tree = Tree::<FsEntry>::new();
    let root = tree
        .insert(
            Node::new(FsEntry {
                path: "/".into(),
                size: 0,
            }),
            id_tree::InsertBehavior::AsRoot,
        )
        .unwrap();

    let mut curr = root;
    for cmd in input.split('$').skip(1) {
        match cmd.trim().lines().next().unwrap() {
            "ls" => {
                for entry in cmd.trim().lines().skip(1) {
                    match entry.split_whitespace().collect_tuple().unwrap() {
                        ("dir", _) => continue,
                        (filesize, filename) => {
                            let node = Node::new(FsEntry {
                                size: filesize.parse::<usize>().unwrap(),
                                path: PathBuf::from(filename.clone()),
                            });
                            tree.insert(node, id_tree::InsertBehavior::UnderNode(&curr))
                                .unwrap();
                        }
                    }
                }
            }
            "cd /" => {
                continue;
            }
            "cd .." => {
                curr = tree.get(&curr).unwrap().parent().unwrap().clone();
            }
            cd_dir => {
                let node = Node::new(FsEntry {
                    path: PathBuf::from(cd_dir.split_once(" ").unwrap().1.clone()),
                    size: 0,
                });
                curr = tree
                    .insert(node, id_tree::InsertBehavior::UnderNode(&curr))
                    .unwrap();
            }
        }
    }
    return tree;
}

pub fn total_size(tree: &Tree<FsEntry>, node: &Node<FsEntry>) -> usize {
    let mut total = node.data().size;
    for child in node.children() {
        total += total_size(tree, tree.get(child).unwrap());
    }

    return total;
}

pub fn part1(input: String) -> usize {
    let tree = dir_maps(input);
    let sum = tree
        .traverse_pre_order(tree.root_node_id().unwrap())
        .unwrap()
        .filter(|n| !n.children().is_empty())
        .map(|n| total_size(&tree, n))
        .filter(|&s| s <= 100_000)
        .sum::<usize>();

    return sum;
}

pub fn part2(input: String) -> usize {
    let tree = dir_maps(input);
    let total_space: usize = 70_000_000;
    let used_space = total_size(&tree, tree.get(tree.root_node_id().unwrap()).unwrap());
    let free_space = total_space.checked_sub(used_space).unwrap();
    let needed_free_space: usize = 30_000_000;
    let minimum_space_to_free = needed_free_space.checked_sub(free_space).unwrap();

    let remove_size = tree
        .traverse_pre_order(tree.root_node_id().unwrap())
        .unwrap()
        .filter(|n| !n.children().is_empty())
        .map(|n| total_size(&tree, n))
        .filter(|&s| s >= minimum_space_to_free)
        .min()
        .unwrap();

    return remove_size;
}
