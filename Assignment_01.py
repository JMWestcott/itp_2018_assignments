{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Introduction to Programming (Summer 2018)\n",
    "## Assignment 1 (Due date: 22nd July 2018 )"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Question 1\n",
    "### Basic mathematical operations\n",
    "\n",
    "Basic mathematical operations between two integers:\n",
    "\n",
    "Using 5 and 7 perform the following operations:\n",
    "+ addition\n",
    "+ subtraction\n",
    "+ multiplication\n",
    "+ division\n",
    "+ power (5^7)\n",
    "\n",
    "You should output the type of the result as well as the result. eg:\n",
    "+ operation: 3 + 2 \n",
    "+ output: < class 'int'> 5"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Addition: <class 'int'> 12\n",
      "Subtraction: <class 'int'> -2\n",
      "Multiplication: <class 'int'> 35\n",
      "Division: <class 'float'> 0.7142857142857143\n",
      "Exponent: <class 'int'> 78125\n"
     ]
    }
   ],
   "source": [
    "a = 5\n",
    "b = 7\n",
    "print('Addition:',type(a+b),(a+b))\n",
    "print('Subtraction:',type(a-b),(a-b))\n",
    "print('Multiplication:',type(a*b),(a*b))\n",
    "print('Division:',type(a/b),(a/b))\n",
    "print('Exponent:',type(a**b),(a**b))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Question 2\n",
    "### Variables\n",
    "\n",
    "Perform the same operations as in Question 1, except use the input() operation to get two integers. In addition store the result of each operation in a variable called result_< operation > eg result_addition for addition."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "number1 = #ADD CODE TO GET FIRST INT\n",
    "number2 = #ADD CODE TO GET SECOND INT\n",
    "\n",
    "# ADDITION\n",
    "# SUBTRACTION\n",
    "# MULTIPLICATION\n",
    "# DIVISION\n",
    "# POWER\n",
    "\n",
    "# THIS IS TO CHECK YOUR CODE, DON'T CHANGE THIS\n",
    "# IF YOUR CODE IS CORRECT YOU WILL NOT GET ANY ERRORS\n",
    "assert result_addition == number1 + number2, \"{} != {} + {}\".format(result_addition, number1, number2)\n",
    "assert result_subtraction == number1 - number2, \"{} != {} - {}\".format(result_addition, number1, number2)\n",
    "assert result_multiplication == number1 * number2, \"{} != {} * {}\".format(result_addition, number1, number2)\n",
    "assert result_division == number1 / number2, \"{} != {} / {}\".format(result_addition, number1, number2)\n",
    "assert result_power == number1 ** number2, \"{} != {} ** {}\".format(result_addition, number1, number2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter first number: 5\n",
      "Enter second number: 7\n",
      "result_addition = 12\n",
      "result_subtraction = -2\n",
      "result_multiplication = 35\n",
      "result_division = 0.7142857142857143\n",
      "result_power = 78125\n"
     ]
    }
   ],
   "source": [
    "number1 = int(input('Enter first number: '))\n",
    "number2 = int(input('Enter second number: '))\n",
    "result_addition = number1 + number2\n",
    "print('result_addition =', result_addition)\n",
    "result_subtraction = number1 - number2\n",
    "print('result_subtraction =', result_subtraction)\n",
    "result_multiplication = number1 * number2\n",
    "print('result_multiplication =', result_multiplication)\n",
    "result_division = number1 / number2\n",
    "print('result_division =', result_division)\n",
    "result_power = number1 ** number2\n",
    "print('result_power =', result_power)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Question 3\n",
    "### Conditionals\n",
    "\n",
    "#### 3.1)\n",
    "Write code to get an integer from the user (assume the user will always enter a integer) as input. If the integer is less than zero print \"The number is negative\" and if the number is greater than or equal to zero print \"The number is positive\"."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter a number: 2\n",
      "The number is positive\n"
     ]
    }
   ],
   "source": [
    "n = int(input('Enter a number: '))\n",
    "if n < 0:\n",
    "    print('The number is negative')\n",
    "if n >= 0:\n",
    "    print('The number is positive')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 3.2)\n",
    "Extend the code from 3.1 to also check whether the number is even or odd. There are four options that can be output by your code now:\n",
    "+ The number is negative and even.\n",
    "+ The number is negative and odd.\n",
    "+ The number is positive and even.\n",
    "+ The number is positive and odd."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter a number: 0\n",
      "The number is positive and even.\n"
     ]
    }
   ],
   "source": [
    "n = int(input('Enter a number: '))\n",
    "if n < 0:\n",
    "    if n%2 == 0:\n",
    "        print('The number is negative and even.')\n",
    "    if n%2 != 0:\n",
    "        print('The number is negative and odd.')\n",
    "if n >= 0:\n",
    "    if n%2 == 0:\n",
    "        print('The number is positive and even.')\n",
    "    if n%2 != 0:\n",
    "        print('The number is positive and odd.')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 3.3)\n",
    "Extend the code from 3.2 to check whether the user has input a integer. If the number is not an integer print \"Error, the value which was input is not an integer\".\n",
    "\n",
    "There are now 5 possible output messages:\n",
    "+ Error, the value which was input is not an integer.\n",
    "+ The number is negative and even.\n",
    "+ The number is negative and odd.\n",
    "+ The number is positive and even.\n",
    "+ The number is positive and odd."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter a number: 2.5\n",
      "Error, the value which was input is not an integer.\n"
     ]
    }
   ],
   "source": [
    "n = input('Enter a number: ')\n",
    "\n",
    "n_valid = True\n",
    "if n.isdigit():\n",
    "    n = int(n)\n",
    "else:\n",
    "    print('Error, the value which was input is not an integer.')\n",
    "    n_valid = False\n",
    "    \n",
    "if n_valid:\n",
    "    if n < 0:\n",
    "        if n%2 == 0:\n",
    "            print('The number is negative and even.')\n",
    "        if n%2 != 0:\n",
    "            print('The number is negative and odd.')\n",
    "    if n >= 0:\n",
    "        if n%2 == 0:\n",
    "            print('The number is positive and even.')\n",
    "        if n%2 != 0:\n",
    "            print('The number is positive and odd.')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Question 4\n",
    "### Looping\n",
    "\n",
    "In lecture 4 we created the code to print squares to the console, these questions will require different shapes to be printed.\n",
    "\n",
    "For each of shapes print using the following characters:\n",
    "+ Start by using only the '*' character\n",
    "+ Use the row index as the character\n",
    "+ Use the column index as the character\n",
    "+ Use the cummulative index as the character\n",
    "\n",
    "**For all of these questions assume that the user will always enter integers and that (1 <= input <= 9)**\n",
    "\n",
    "### Example (printing a square of size 'n'):"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the width of the square3\n",
      "* Character\n",
      "---------\n",
      "***\n",
      "***\n",
      "***\n",
      "Row Index\n",
      "---------\n",
      "  0  0  0\n",
      "  1  1  1\n",
      "  2  2  2\n",
      "Column Index\n",
      "---------\n",
      "  0  1  2\n",
      "  0  1  2\n",
      "  0  1  2\n",
      "Cumulative Index\n",
      "---------\n",
      "  0  1  2\n",
      "  3  4  5\n",
      "  6  7  8\n"
     ]
    }
   ],
   "source": [
    "n = int(input(\"Enter n\"))\n",
    "\n",
    "# USING '*' AS THE CHARACTER\n",
    "print('* Character\\n---------')\n",
    "for j in range(n):\n",
    "    line = ''\n",
    "    for i in range(n):\n",
    "        line += '*'\n",
    "    print(line)\n",
    "    \n",
    "# USING THE ROW INDEX AS THE CHARACTER\n",
    "print('Row Index\\n---------')\n",
    "for j in range(n):\n",
    "    line = ''\n",
    "    for i in range(n):\n",
    "        line += '{:>3}'.format(j)\n",
    "    print(line)\n",
    "    \n",
    "# USING THE COL INDEX AS THE CHARACTER\n",
    "print('Column Index\\n---------')\n",
    "for j in range(n):\n",
    "    line = ''\n",
    "    for i in range(n):\n",
    "        line += '{:>3}'.format(i)\n",
    "    print(line)\n",
    "\n",
    "# USING THE CUMULATIVE INDEX AS THE CHARACTER\n",
    "print('Cumulative Index\\n---------')\n",
    "for j in range(n):\n",
    "    line = ''\n",
    "    for i in range(n):\n",
    "        line += '{:>3}'.format(j * n + i)\n",
    "    print(line)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 4.1)\n",
    "Print a triangle with height and width **n**\n",
    "\n",
    "**eg:**: n = 5\n",
    "```\n",
    "*\n",
    "**\n",
    "***\n",
    "****\n",
    "*****\n",
    "\n",
    "  0\n",
    "  1  1\n",
    "  2  2  2\n",
    "  3  3  3  3\n",
    "  4  4  4  4  4\n",
    "\n",
    "  0\n",
    "  0  1\n",
    "  0  1  2\n",
    "  0  1  2  3\n",
    "  0  1  2  3  4\n",
    "\n",
    "  0\n",
    "  1  2\n",
    "  3  4  5\n",
    "  6  7  8  9 \n",
    " 10 11 12 13 14\n",
    "\n",
    "```"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "n = int(input(\"Enter n\"))\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 4.1)\n",
    "Print a rectangle with height **n** and width **m**\n",
    "\n",
    "**eg:**: n = 3, m = 2\n",
    "```\n",
    "***\n",
    "***\n",
    "***\n",
    "\n",
    "  0  1\n",
    "  1  1\n",
    "  2  2\n",
    "\n",
    "  0  1\n",
    "  0  1\n",
    "  0  1\n",
    "\n",
    "  0  1\n",
    "  2  3\n",
    "  4  5\n",
    "```"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "n = int(input(\"Enter n\"))\n",
    "m = int(input(\"Enter m\"))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Question 5\n",
    "### Finding Prime Numbers\n",
    "\n",
    "Write code which finds all of the prime numbers between 1 and 100 and stores them in a list.\n",
    "Print the list of prime numbers.\n",
    "\n",
    "A prime number is a number which is only divisible by itself and 1.\n",
    "\n",
    "Some starting code has been provided."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 2, 3, 4, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]\n"
     ]
    }
   ],
   "source": [
    "results = []\n",
    "for i in range(1, 101):\n",
    "    prime = True\n",
    "    for j in range(2, i//2):\n",
    "        if #COMPLETE#:\n",
    "            prime = False\n",
    "    #COMPLETE#\n",
    "print(results)\n",
    "# expected output: [1, 2, 3, 4, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Question 6\n",
    "### git and github\n",
    "\n",
    "1. Create a directory called 'assignments' for all of the homework assignments.\n",
    "    + **Do not** make this directory in the 2018_ITP directory which contains the lecture material\n",
    "2. Add this Jupyter notebook to the directory you just created\n",
    "3. Initialize this directory as a git repository\n",
    "4. Add your assignment notebook to the repository\n",
    "5. Commit your assignment\n",
    "6. On github.com create a new repository called itp_2018_assigments\n",
    "7. Link the github repository with your local repository\n",
    "8. Email the link to your github repository to Mark.Grivainis@nyumc.org and Himanshu.Grover@nyumc.org\n",
    "\n",
    "All of your homework will be added to this repository, you will need to have pushed your changes before the deadline for any of the assignments."
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
