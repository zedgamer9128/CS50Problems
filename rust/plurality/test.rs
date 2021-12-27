#[cfg(test)]
mod test {
    #[test]
    fn test_vote() {
        use super::*;
        use std::env::args;
        unsafe {
            
            let args = args().collect::<Vec<String>>();
            if args.len() != 4 {
                println!("Usage: cargo test [candidate ...]");
                return;
            }

            let setup = args[2].clone().parse::<i32>().unwrap();
            let test = args[3].clone().parse::<i32>().unwrap();

            if setup == 0 {
                CANDIDATE_COUNT = 3;
                CANDIDATES.push(Candidate::new(String::from("Alice"), 0));
                CANDIDATES.push(Candidate::new(String::from("Bob"), 0));
                CANDIDATES.push(Candidate::new(String::from("Charlie"), 0));
            }

            if test == 0 {
                assert_eq!(vote(&String::from("Alice")), true);
            } else if test == 1 {
                assert_eq!(vote(&String::from("Bob")), true);
            } else if test == 2 {
                assert_eq!(vote(&String::from("Charlie")), true);
            } else if test == 3 {
                assert_eq!(vote(&String::from("Dave")), false);
            } else if test == 4 {
                vote(&String::from("Alice"));
                print!(
                    "{} {} {}",
                    CANDIDATES[0].name, CANDIDATES[0].votes, CANDIDATES[1].votes
                );
            } else if test == 5 {
                CANDIDATES[0].votes = 2;
                CANDIDATES[1].votes = 7;
                CANDIDATES[2].votes = 0;
                vote(&String::from("Bob"));
                print!(
                    "{} {} {}",
                    CANDIDATES[0].name, CANDIDATES[0].votes, CANDIDATES[1].votes
                );
            } else if test == 6 {
                CANDIDATES[0].votes = 2;
                CANDIDATES[1].votes = 8;
                CANDIDATES[2].votes = 0;
                vote(&String::from("David"));
                print!(
                    "{} {} {}",
                    CANDIDATES[0].name, CANDIDATES[0].votes, CANDIDATES[1].votes
                );
            } else if test == 7 {
                CANDIDATES[0].votes = 8;
                CANDIDATES[1].votes = 2;
                CANDIDATES[2].votes = 0;
                print_winner();
            } else if test == 8 {
                CANDIDATES[0].votes = 1;
                CANDIDATES[1].votes = 8;
                CANDIDATES[2].votes = 2;
                print_winner();
            } else if test == 9 {
                CANDIDATES[0].votes = 1;
                CANDIDATES[1].votes = 8;
                CANDIDATES[2].votes = 9;
                print_winner();
            } else if test == 10 {
                CANDIDATES[0].votes = 8;
                CANDIDATES[1].votes = 8;
                CANDIDATES[2].votes = 5;
                print_winner();
            } else if test == 11 {
                CANDIDATES[0].votes = 8;
                CANDIDATES[1].votes = 8;
                CANDIDATES[2].votes = 8;
                print_winner();
            }
        }
    }
}
