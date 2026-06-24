# questions.py

questions = {
    "Array/String": [
        {"name": "Merge Strings Alternately", "completed": False},
        {"name": "Greatest Common Divisor of Strings", "completed": False},
        {"name": "Kids With the Greatest Number of Candies", "completed": False},
        {"name": "Can Place Flowers", "completed": False},
        {"name": "Reverse Vowels of a String", "completed": False},
        {"name": "Reverse Words in a String", "completed": False},
        {"name": "Product of Array Except Self", "completed": False},
        {"name": "Increasing Triplet Subsequence", "completed": False},
        {"name": "String Compression", "completed": False}
    ],

    "Two Pointers": [
        {"name": "Move Zeroes", "completed": False},
        {"name": "Is Subsequence", "completed": False},
        {"name": "Container With Most Water", "completed": False},
        {"name": "Max Number of K-Sum Pairs", "completed": False}
    ],

    "Sliding Window": [
        {"name": "Maximum Average Subarray I", "completed": False},
        {"name": "Maximum Number of Vowels in a Substring", "completed": False},
        {"name": "Max Consecutive Ones III", "completed": False},
        {"name": "Longest Subarray of 1's After Deleting One Element", "completed": False}
    ],

    "Prefix Sum": [
        {"name": "Find the Highest Altitude", "completed": False},
        {"name": "Find Pivot Index", "completed": False}
    ],

    "Hash Map/Set": [
        {"name": "Find the Difference of Two Arrays", "completed": False},
        {"name": "Unique Number of Occurrences", "completed": False},
        {"name": "Determine if Two Strings Are Close", "completed": False},
        {"name": "Equal Row and Column Pairs", "completed": False}
    ],

    "Stack": [
        {"name": "Removing Stars From a String", "completed": False},
        {"name": "Asteroid Collision", "completed": False},
        {"name": "Decode String", "completed": False}
    ],

    "Queue": [
        {"name": "Number of Recent Calls", "completed": False},
        {"name": "Dota2 Senate", "completed": False}
    ],

    "Linked List": [
        {"name": "Delete the Middle Node of a Linked List", "completed": False},
        {"name": "Odd Even Linked List", "completed": False},
        {"name": "Reverse Linked List", "completed": False},
        {"name": "Maximum Twin Sum of a Linked List", "completed": False}
    ],

    "Binary Tree DFS": [
        {"name": "Maximum Depth of Binary Tree", "completed": False},
        {"name": "Leaf-Similar Trees", "completed": False},
        {"name": "Count Good Nodes in Binary Tree", "completed": False},
        {"name": "Path Sum III", "completed": False}
    ],

    "Binary Tree BFS": [
        {"name": "Binary Tree Right Side View", "completed": False},
        {"name": "Maximum Level Sum of a Binary Tree", "completed": False}
    ],

    "Binary Search Tree": [
        {"name": "Search in a BST", "completed": False},
        {"name": "Delete Node in a BST", "completed": False}
    ],

    "Graphs DFS": [
        {"name": "Keys and Rooms", "completed": False},
        {"name": "Number of Provinces", "completed": False},
        {"name": "Reorder Routes to Make All Paths Lead to the City Zero", "completed": False}
    ],

    "Graphs BFS": [
        {"name": "Nearest Exit from Entrance in Maze", "completed": False},
        {"name": "Rotting Oranges", "completed": False}
    ],

    "Heap/Priority Queue": [
        {"name": "Kth Largest Element in an Array", "completed": False},
        {"name": "Smallest Number in Infinite Set", "completed": False},
        {"name": "Maximum Subsequence Score", "completed": False}
    ],

    "Binary Search": [
        {"name": "Guess Number Higher or Lower", "completed": False},
        {"name": "Successful Pairs of Spells and Potions", "completed": False},
        {"name": "Find Peak Element", "completed": False}
    ],

    "Backtracking": [
        {"name": "Letter Combinations of a Phone Number", "completed": False},
        {"name": "Combination Sum III", "completed": False}
    ],

    "Dynamic Programming": [
        {"name": "N-th Tribonacci Number", "completed": False},
        {"name": "Min Cost Climbing Stairs", "completed": False},
        {"name": "House Robber", "completed": False},
        {"name": "Domino and Tromino Tiling", "completed": False}
    ],

    "Bit Manipulation": [
        {"name": "Counting Bits", "completed": False},
        {"name": "Single Number", "completed": False}
    ],

    "Intervals": [
        {"name": "Non-overlapping Intervals", "completed": False}
    ],

    "Monotonic Stack": [
        {"name": "Daily Temperatures", "completed": False},
        {"name": "Online Stock Span", "completed": False}
    ],

    "Trie": [
        {"name": "Implement Trie (Prefix Tree)", "completed": False},
        {"name": "Search Suggestions System", "completed": False}
    ]
}



difficulty_map = {
    "Merge Strings Alternately": "Easy",
    "Greatest Common Divisor of Strings": "Easy",
    "Kids With the Greatest Number of Candies": "Easy",
    "Can Place Flowers": "Easy",
    "Reverse Vowels of a String": "Easy",
    "Reverse Words in a String": "Medium",
    "Product of Array Except Self": "Medium",
    "Increasing Triplet Subsequence": "Medium",
    "String Compression": "Medium",

    "Move Zeroes": "Easy",
    "Is Subsequence": "Easy",
    "Container With Most Water": "Medium",
    "Max Number of K-Sum Pairs": "Medium",

    "Maximum Average Subarray I": "Easy",
    "Maximum Number of Vowels in a Substring": "Medium",
    "Max Consecutive Ones III": "Medium",
    "Longest Subarray of 1's After Deleting One Element": "Medium",

    "Find the Highest Altitude": "Easy",
    "Find Pivot Index": "Easy",

    "Find the Difference of Two Arrays": "Easy",
    "Unique Number of Occurrences": "Easy",
    "Determine if Two Strings Are Close": "Medium",
    "Equal Row and Column Pairs": "Medium",

    "Removing Stars From a String": "Medium",
    "Asteroid Collision": "Medium",
    "Decode String": "Medium",

    "Number of Recent Calls": "Easy",
    "Dota2 Senate": "Medium",

    "Delete the Middle Node of a Linked List": "Medium",
    "Odd Even Linked List": "Medium",
    "Reverse Linked List": "Easy",
    "Maximum Twin Sum of a Linked List": "Medium",

    "Maximum Depth of Binary Tree": "Easy",
    "Leaf-Similar Trees": "Easy",
    "Count Good Nodes in Binary Tree": "Medium",
    "Path Sum III": "Medium",

    "Binary Tree Right Side View": "Medium",
    "Maximum Level Sum of a Binary Tree": "Medium",

    "Search in a BST": "Easy",
    "Delete Node in a BST": "Medium",

    "Keys and Rooms": "Medium",
    "Number of Provinces": "Medium",
    "Reorder Routes to Make All Paths Lead to the City Zero": "Medium",

    "Nearest Exit from Entrance in Maze": "Medium",
    "Rotting Oranges": "Medium",

    "Kth Largest Element in an Array": "Medium",
    "Smallest Number in Infinite Set": "Medium",
    "Maximum Subsequence Score": "Hard",

    "Guess Number Higher or Lower": "Easy",
    "Successful Pairs of Spells and Potions": "Medium",
    "Find Peak Element": "Medium",

    "Letter Combinations of a Phone Number": "Medium",
    "Combination Sum III": "Medium",

    "N-th Tribonacci Number": "Easy",
    "Min Cost Climbing Stairs": "Easy",
    "House Robber": "Medium",
    "Domino and Tromino Tiling": "Medium",

    "Counting Bits": "Easy",
    "Single Number": "Easy",

    "Non-overlapping Intervals": "Medium",

    "Daily Temperatures": "Medium",
    "Online Stock Span": "Medium",

    "Implement Trie (Prefix Tree)": "Medium",
    "Search Suggestions System": "Medium"
}

for topic in questions:
    for q in questions[topic]:
        q["difficulty"] = difficulty_map.get(
            q["name"],
            "Unknown"
        )