# -*- coding: utf-8 -*-
"""temp_tracker

Implements a solution to `Temperature Tracker`_ problem, problem 7, from Interview Cake.

Givens:
    * class name to implement, TempTracker
    * TempTracker's methods and their returns

Guidance:
    * Optimize space
        * Store as little of the input temperatures as possible
    * Optimize getter running time versus setters
        * Compute as many of the values on insert as possible so that getting is fast
        * If the median was necessary, a bisect algorithm perhaps with the bisect module would be applicable
            * A bisect algorithm could keep an ordered list

.. _Temperature Tracker:
    https://www.interviewcake.com/question/python/temperature-tracker

"""
from typing import *
from collections import defaultdict
import unittest

class Temperature(object):
    """Represents a temperature measurement in degrees and number of times seen.

    Public attributes:
        degrees: degrees given. No units specified in this problem.
        count: the number of times this t˚emperature has been seen. Used to find mode quickly.
    """
    def __init__(self):
        self._degrees = None
        self._count = 1

    @property
    def degrees(self) -> float:
        return self._degrees

    @degrees.setter
    def degrees(self, degrees: float):
        self._degrees = degrees

    @property
    def count(self) -> int:
        return self._count

    @count.setter
    def count(self, count: int):
        self._count = count


class TempTracker(object):
    """Represents a collection of Temperature objects with some elementary statistics.
    
    """
    def __init__(self):
        self.temps = defaultdict(Temperature) # type: DefaultDict[Float,Temperature]
        self.temps_seen_so_far_count = 0
        self.temps_seen_so_far_sum = 0.0
        self.max = Temperature()
        self.min = Temperature()
        self.mean = float
        self.mode_temp = Temperature()

    def insert(self, input_temperature: Union[int,float]) -> int:
        """Records a new tempature

        To optimize getter methods, mode, mean, min and max are computed on insert.

        """
        new_temp = Temperature()
        temperature = float(input_temperature)
        new_temp.degrees = temperature

        # Compute the Mode
        if temperature in self.temps.keys():
            self.temps[temperature].count += 1
        else:
            self.temps[temperature] = new_temp
        
        if self.temps[temperature].count > self.mode_temp.count:
            self.mode_temp = self.temps[temperature]

        # Compute the max
        if not self.max.degrees:
            self.max.degrees = temperature
        elif temperature > self.max.degrees:
            self.max.degrees = temperature

        # Computer the min
        if not self.min.degrees:
            self.min.degrees = temperature
        elif temperature < self.min.degrees:
            self.min.degrees = temperature

        # Compute the mean
        self.temps_seen_so_far_count += 1
        self.temps_seen_so_far_sum += temperature

        self.mean = self.temps_seen_so_far_sum / self.temps_seen_so_far_count

        return 0


    def get_max(self) -> float:
        """Returns the highest temp seen so far

        Raises:
            LookupError: if no temps inserted

        """
        if len(self.temps) == 0:
            raise LookupError("Could not computer because no temperatures have been tracked!")
            
        return self.max.degrees

    def get_min(self) -> float:
        """Returns the lowest temp seen so far

        Raises:
            LookupError: if no temps inserted

        """
        if len(self.temps) == 0:
            raise LookupError("Could not computer because no temperatures have been tracked!")


        return self.min.degrees

    def get_mean(self) -> float:
        """Returns the mean of all temps seen so far

        Raises:
            LookupError: if no temps inserted

        """
        if len(self.temps) == 0:
            raise LookupError("Could not computer because no temperatures have been tracked!")


        return self.mean

    def get_mode(self) -> float:
        """Returns a mode of all temps we've seen so far

        Although there may be multiple candidate modes, any mode is acceptable.
        Raises:
            LookupError: if no temps inserted

        """
        if len(self.temps) == 0:
            raise LookupError("Could not computer because no temperatures have been tracked!")

        return self.mode_temp.degrees


if __name__ == '__main__':
    tracker = TempTracker()
    print(tracker.insert(1))
