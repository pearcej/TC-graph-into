"""text example of an iterator
Author: Dr. Jan Pearce, Berea College
Distributed under the GNU General Public License at gnu.org/licenses/gpl.html.
"""

def main():
    x = iter([10, 20, 30, 40])
    print(next(x))
    print(next(x))
    print(next(x))

main()