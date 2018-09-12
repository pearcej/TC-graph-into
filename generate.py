"""text example of a generator
Author: Allen B. Downey
modified from Think Complexity, http://www.greenteapress.com/complexity/html/
Distributed under the GNU General Public License at gnu.org/licenses/gpl.html.
"""

def generate_letters():
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        yield letter

def main():
    iter = generate_letters()
    print(next(iter))
    print(next(iter))
    print(next(iter))

main()