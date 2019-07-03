{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Python 3.7.3 (default, Mar 27 2019, 22:11:17) \r\n",
      "[GCC 7.3.0] :: Anaconda, Inc. on linux\r\n",
      "Type \"help\", \"copyright\", \"credits\" or \"license\" for more information.\r\n",
      ">>> "
     ]
    }
   ],
   "source": [
    "!/usr/bin/env python"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "class Person:\n",
    "    def __init__(self, name, job = None, pay = 0):\n",
    "        self.name = name\n",
    "        self.job = job\n",
    "        self.pay = pay"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## testing the class\n"
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
      "Bob Smith\n",
      "Sue Jones 100000\n"
     ]
    }
   ],
   "source": [
    "bob = Person('Bob Smith')\n",
    "sue = Person('Sue Jones', job = 'dev', pay = 100000)\n",
    "print(bob.name)\n",
    "print(sue.name, sue.pay)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
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
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
