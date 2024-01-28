use std::{
    fs::File,
    io::{self, Read},
};

fn read_file(file_name: &str) -> Result<String, io::Error> {
    let f = File::open(file_name);

    let mut f = match f {
        Ok(file) => file,
        Err(e) => return Err(e),
    };

    let mut s = String::new();

    match f.read_to_string(&mut s) {
        Ok(_) => return Ok(s),
        Err(e) => return Err(e),
    }
}

fn part1() {
    let mut stair_count = 0;
    let contents = read_file("input");
    for c in contents.unwrap().chars() {
        if c == '(' {
            stair_count += 1;
        } else if c == ')' {
            stair_count -= 1;
        }
    }
    println!("P1: {}", stair_count);
}

fn part2() {
    let mut stair_count = 0;
    let mut position = 0;
    let contents = read_file("input");
    for c in contents.unwrap().chars() {
        position += 1;
        if c == '(' {
            stair_count += 1;
        } else if c == ')' {
            stair_count -= 1;
        }
        if stair_count == -1 {
            println!("P2: {}", position);
            break;
        }
    }
}

fn main() {
    part1();
    part2();
}
