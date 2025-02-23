#!/bin/bash

# Prompt user for input
read -p "Enter a number: " number

# Check if the number is less than 2
if [ "$number" -lt 2 ]; then
    echo "$number is not a prime number."
    exit
fi

# Initialize a variable to track divisibility
is_prime=1

# Check for factors from 2 to the square root of the number
for ((i = 2; i * i <= number; i++)); do
    if [ $((number % i)) -eq 0 ]; then
        is_prime=0
        break
    fi
done

# Output result based on divisibility check
if [ $is_prime -eq 1 ]; then
    echo "$number is a prime number."
else
    echo "$number is not a prime number."
fi
