use std::{
    fs::File,
    io::{self, Read},
};

fn read_file(file_name: &str) -> Result<String, io::Error> {
    let file = File::open(file_name);

    let mut f = match file {
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
    let contents = read_file("input");
}

fn main() {
    part1();
}
