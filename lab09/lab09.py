def insert_into_all(item, nested_list):
    return [[item] + child for child in nested_list]
    """Assuming that nested_list is a list of lists, return a new list
    consisting of all the lists in nested_list, but with item added to
    the front of each.

    >>> nl = [[], [1, 2], [3]]
    >>> insert_into_all(0, nl)
    [[0], [0, 1, 2], [0, 3]]
    """
    return [[item] + child for child in nested_list]

    """Assuming that S is a list, return a nested list of all subsequences
    of S (a list of lists). The subsequences can appear in any order.【

    >>> seqs = subseqs([1, 2, 3])
    >>> sorted(seqs)
    [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
    >>> subseqs([])
    [[]]
    """
def subseqs(s):
    if len(s) < 1:
        return [[]]
    else:
        #分为2种 一种是去掉first的所有子序列集合
        subsequence = subseqs(s[1:])
        #一种是加上
        with_first= insert_into_all(s[0], subsequence)
    return subsequence + with_first


def subseqs(s):
    if len(s) < 1:
        return [[]]
    else:
        #获取去掉第一个元素的所有子序列
        subsequense = subseqs(s[1:])
        #将第一个元素插入所有子序列的开头
        with_first = insert_into_all(s[0],subsequense)
        #返回包含和不包含第一个元素的所有子序列
        return subsequense + with_first


def subseqs(s):
    if len(s) <1 :
        return [[]]
    else:
        #先找到剔除第一个元素的其他所有子序列
        subsequences = subseqs(s[1:])
        #将第一个元素添加到所有的子序列
        with_first = insert_into_all(s[0],subsequences)
        #将包含第一个的序列和不包含第一个序列相加
        return subsequences + with_first

        
#非递减序列
def inc_subseqs(s):
    """Assuming that S is a list, return a nested list of all subsequences
    of S (a list of lists) for which the elements of the subsequence
    are strictly nondecreasing. The subsequences can appear in any order.

    >>> seqs = inc_subseqs([1, 3, 2])
    >>> sorted(seqs)
    [[], [1], [1, 2], [1, 3], [2], [3]]
    >>> inc_subseqs([])
    [[]]
    >>> seqs2 = inc_subseqs([1, 1, 2])
    >>> sorted(seqs2)
    [[], [1], [1], [1, 1], [1, 1, 2], [1, 2], [1, 2], [2]]
    """
def inc_subseqs(s):
    def subseq_helper(s, prev):
        if not s:
            return[[]]
        elif s[0] < prev:
            return subseq_helper(s[1:],prev)
        else:
            a = subseq_helper(s[1:],s[0]) #包含当前元素s[0]
            b = subseq_helper(s[1:],prev) #不包含当前元素s[0]
            return insert_into_all(s[0], a) + b 
    return subseq_helper(s, float('-inf'))


def inc_subseqs(s):
    """Assuming that S is a list, return a nested list of all subsequences
    of S (a list of lists) for which the elements of the subsequence
    are strictly nondecreasing. The subsequences can appear in any order.

    >>> seqs = inc_subseqs([1, 3, 2])
    >>> sorted(seqs)
    [[], [1], [1, 2], [1, 3], [2], [3]]
    >>> inc_subseqs([])
    [[]]
    >>> seqs2 = inc_subseqs([1, 1, 2])
    >>> sorted(seqs2)
    [[], [1], [1], [1, 1], [1, 1, 2], [1, 2], [1, 2], [2]]
    """
def inc_subseqs(s):
    def subseq_helper(s, prev):
        if not s:
            return [[]]
        elif s[0] < prev:
            return subseq_helper(s[1:],prev)
        else:
            a = subseq_helper(s[1:],s[0]) #一种是不跳过s[0]的 按照正常的顺序
            b = subseq_helper(s[1:],prev)
            return insert_into_all(s[0], a) + b
    return subseq_helper(s, float('inf'))


def num_trees(n):
    """How many full binary trees have exactly n leaves? E.g.,

    1   2        3       3    ...
    *   *        *       *
       / \      / \     / \
      *   *    *   *   *   *
              / \         / \
             *   *       *   *

    >>> num_trees(1)
    1
    >>> num_trees(2)
    1
    >>> num_trees(3)
    2
    >>> num_trees(8)
    429

    """
def num_trees(n): #卡特兰数
    if  n == 1 or n == 2:
        return 1
    total = 0
    for k in range(1,n):
        total += num_trees(k) * num_trees(n-k)
    return total

def num_trees(n): 
    if n == 1:
        return 1
    total = 0
    for how_many_on_left in range(1,n):
        how_many_on_right = n - how_many_on_left
        num_on_left = num_trees(how_many_on_left)
        num_on_right = num_trees(how_many_on_right)
        total += num_on_left*num_on_right
    return total


def num_trees(n): 
    if n == 1 or n == 2:
        return 1
    total = 0
    for how_many_on_left in range(1,n):
        how_many_on_right = n - how_many_on_left
        num_on_left = num_trees(how_many_on_left)
        num_on_right = num_trees(how_many_on_right)
        total += num_on_left*num_on_right
    return total





def make_generators_generator(g):
    """Generates all the "sub"-generators of the generator returned by
    the generator function g.

    >>> def every_m_ints_to(n, m):
    ...     i = 0
    ...     while (i <= n):
    ...         yield i
    ...         i += m
    ...
    >>> def every_3_ints_to_10():
    ...     for item in every_m_ints_to(10, 3):
    ...         yield item
    ...
    >>> for gen in make_generators_generator(every_3_ints_to_10):
    ...     print("Next Generator:")
    ...     for item in gen:
    ...         print(item)
    ...
    Next Generator:
    0
    Next Generator:
    0
    3
    Next Generator:
    0
    3
    6
    Next Generator:
    0
    3
    6
    9
    """
def make_generators_generator(g):
    elements = list(g()) #把原先生成器的元素都取出来

    def gen(i):
        for j in range(i): #产生前i个元素
            yield elements[j]
    
    for i in range(1,len(elements)+1):#从1到元素的个数
        yield gen(i) #每次都产生一个子生成器

def make_generators_generator(g):
    elements = list(g()) #把原先生成器的元素都取出来
    def gen(i):
        for j in range(i): #产生前i个元素
            yield elements[j]
    for i in range(1,len(elements)+1): #返回一个生成器
        return gen(i)

class Button:
    """
    Represents a single button
    """
    def __init__(self, pos, key):
        """
        Creates a button
        """
        self.pos = pos
        self.key = key
        self.times_pressed = 0


    
    """A Keyboard takes in an arbitrary amount of buttons, and has a
    dictionary of positions as keys, and values as Buttons.

    >>> b1 = Button(0, "H")
    >>> b2 = Button(1, "I")
    >>> k = Keyboard(b1, b2)
    >>> k.buttons[0].key
    'H'
    >>> k.press(1)
    'I'
    >>> k.press(2) #No button at this position
    ''
    >>> k.typing([0, 1])
    'HI'
    >>> k.typing([1, 0])
    'IH'
    >>> b1.times_pressed
    2
    >>> b2.times_pressed
    3
    """
class Keyboard:
    def __init__(self, *args):
        self.buttons = {}
        for button in args:#把对象传入args 遍历元祖
            self.buttons[button.pos] = button
    def press(self, info):
        """Takes in a position of the button pressed, and
        returns that button's output"""
        if info in self.buttons:
            self.buttons[info].times_pressed +=1
            return self.buttons[info].key
        else:
            return ''
    def typing(self, typing_input):
        """Takes in a list of positions of buttons presse
        d, and
        returns the total output"""
        ans = ''
        for word in typing_input:
            ans += self.buttons[word].key
            self.buttons[word].times_pressed +=1
        return ans


def make_advanced_counter_maker():
    """Makes a function that makes counters that understands the
    messages "count", "global-count", "reset", and "global-reset".
    See the examples below:

    >>> make_counter = make_advanced_counter_maker()
    >>> tom_counter = make_counter()
    >>> tom_counter('count')
    1
    >>> tom_counter('count')
    2
    >>> tom_counter('global-count')
    1
    >>> jon_counter = make_counter()
    >>> jon_counter('global-count')
    2
    >>> jon_counter('count')
    1
    >>> jon_counter('reset')
    >>> jon_counter('count')
    1
    >>> tom_counter('count')
    3
    >>> jon_counter('global-count')
    3
    >>> jon_counter('global-reset')
    >>> tom_counter('global-count')
    1
    """
def make_advanced_counter_maker():
    global_count = 0 #全局计数器
    def make_counter():
        local_count = 0 #每个counter的局部计数器
        def counter(message):
            nonlocal local_count,global_count
            if message == 'count':
                local_count += 1
                return local_count
            elif message == 'reset':
                local_count = 0
            elif message == 'global-count':
                global_count += 1
                return global_count
            elif message == 'global-reset':
                global_count = 0
            else:
                return None
        return counter
    return make_counter

#Q8:Mutable Lists

def trade(first, second):
    """Exchange the smallest prefixes of first and second that have equal sum.

    >>> a = [1, 1, 3, 2, 1, 1, 4]
    >>> b = [4, 3, 2, 7]
    >>> trade(a, b) # Trades 1+1+3+2=7 for 4+3=7
    'Deal!'
    >>> a
    [4, 3, 1, 1, 4]
    >>> b
    [1, 1, 3, 2, 2, 7]
    >>> c = [3, 3, 2, 4, 1]
    >>> trade(b, c)
    'No deal!'
    >>> b
    [1, 1, 3, 2, 2, 7]
    >>> c
    [3, 3, 2, 4, 1]
    >>> trade(a, c)
    'Deal!'
    >>> a
    [3, 3, 2, 1, 4]
    >>> b
    [1, 1, 3, 2, 2, 7]
    >>> c
    [4, 3, 1, 4, 1]
    """
def trade(first, second):
    m, n = 1, 1
    equal_prefix = lambda: (sum(first[:m]) == sum(second[:n]) and m <= len(first) and n<= len(second))
    while not equal_prefix():
        if m > len(first) or n > len(second):
            return 'No Deal'
        if sum(first[:m]) < sum(second[:n]):
            m += 1
        else:
            n += 1
    first[:m], second[:n] = second[:n], first[:m]
    return 'Deal!'


def card(n):
    """Return the playing card numeral as a string for a positive n <= 13."""
    assert type(n) == int and n > 0 and n <= 13, "Bad card n"
    specials = {1: 'A', 11: 'J', 12: 'Q', 13: 'K'}
    return specials.get(n, str(n))

def shuffle(cards):
    """Return a shuffled list that interleaves the two halves of cards.

    >>> shuffle(range(6))
    [0, 3, 1, 4, 2, 5]
    >>> suits = ['♡', '♢', '♤', '♧']
    >>> cards = [card(n) + suit for n in range(1,14) for suit in suits]
    >>> cards[:12]
    ['A♡', 'A♢', 'A♤', 'A♧', '2♡', '2♢', '2♤', '2♧', '3♡', '3♢', '3♤', '3♧']
    >>> cards[26:30]
    ['7♤', '7♧', '8♡', '8♢']
    >>> shuffle(cards)[:12]
    ['A♡', '7♤', 'A♢', '7♧', 'A♤', '8♡', 'A♧', '8♢', '2♡', '8♤', '2♢', '8♧']
    >>> shuffle(shuffle(cards))[:12]
    ['A♡', '4♢', '7♤', '10♧', 'A♢', '4♤', '7♧', 'J♡', 'A♤', '4♧', '8♡', 'J♢']
    >>> cards[:12]  # Should not be changed
    ['A♡', 'A♢', 'A♤', 'A♧', '2♡', '2♢', '2♤', '2♧', '3♡', '3♢', '3♤', '3♧']
    """
def shuffle(cards):
    assert len(cards) % 2 == 0, 'len(cards) must be even'
    half = cards[len(cards)//2:]
    shuffled = []
    for i in range(len(half)):
        shuffled.append(cards[i])
        shuffled.append(half[i])
    return shuffled


def insert(link, value, index):
    """Insert a value into a Link at the given index.

    >>> link = Link(1, Link(2, Link(3)))
    >>> print(link)
    <1 2 3>
    >>> insert(link, 9001, 0)
    >>> print(link)
    <9001 1 2 3>
    >>> insert(link, 100, 2)
    >>> print(link)
    <9001 1 100 2 3>
    >>> insert(link, 4, 5)
    IndexError
    """
def insert(link, value, index):
    if index == 0:
        new_node= Link(value,link)
        return new_node
    curr = link
    for _ in range(index-1):
        if curr.rest is Link.empty:
            raise IndexError
        cur = cur.rest
    curr.rest = Link(value,curr.rest)
    return link

def insert(link, value, index):
    if index == 0 :
        newnode = Link(value,link)
        return newnode
    curr= link
    for _ in range(index-1):
        if cur.rest is Link.empty:
            return IndexError
        cur = cur.rest
    cur.rest = Link(value,cur.rest)
    return link

        

            



def deep_len(lnk):
    """ Returns the deep length of a possibly deep linked list.

    >>> deep_len(Link(1, Link(2, Link(3))))
    3
    >>> deep_len(Link(Link(1, Link(2)), Link(3, Link(4))))
    4
    >>> levels = Link(Link(Link(1, Link(2)), \
            Link(3)), Link(Link(4), Link(5)))
    >>> print(levels)
    <<<1 2> 3> <4> 5>
    >>> deep_len(levels)
    5
    """
def deep_len(lnk):
    if lnk is Link.empty:
        return 0
    first_len_count = deep_len(lnk.first) if isinstance(lnk.first,Link) else 1
    rest_len_count = deep_len(lnk.rest)
    return first_len_count+rest_len_count


def deep_len(lnk):
    if lnk is Link.empty:
        return 0
    first_len = deep_len(lnk.first) if isinstance(lnk.first,Link) else 1
    second_len = deep_len(lnk.rest)
    return first_len + second_len



def make_to_string(front, mid, back, empty_repr):
    """ Returns a function that turns linked lists to strings.

    >>> kevins_to_string = make_to_string("[", "|-]-->", "", "[]")
    >>> jerrys_to_string = make_to_string("(", " . ", ")", "()")
    >>> lst = Link(1, Link(2, Link(3, Link(4))))
    >>> kevins_to_string(lst)
    '[1|-]-->[2|-]-->[3|-]-->[4|-]-->[]'
    >>> kevins_to_string(Link.empty)
    '[]'
    >>> jerrys_to_string(lst)
    '(1 . (2 . (3 . (4 . ()))))'
    >>> jerrys_to_string(Link.empty)
    '()'
    """
def make_to_string(front, mid, back, empty_repr):
    def printer(lnk):
        if lnk is Link.empty:
            return empty_repr
        else:
            return front + str(lnk.first) + mid + printer(lnk.rest)+ back
    return printer


def prune_small(t, n):
    #对于当前节点去剔除
    while t.branches > n:
        largest = max(t.branches, key = lambda b : b.label)
        t.branches.remove(largest) #不停的把最大的剔除
    #递归到下一个子节点
    for b in t.branches:
        prune_small(b,n)
    """Prune the tree mutatively, keeping only the n branches
    of each node with the smallest label.

    >>> t1 = Tree(6)
    >>> prune_small(t1, 2)
    >>> t1
    Tree(6)
    >>> t2 = Tree(6, [Tree(3), Tree(4)])
    >>> prune_small(t2, 1)
    >>> t2
    Tree(6, [Tree(3)])
    >>> t3 = Tree(6, [Tree(1), Tree(3, [Tree(1), Tree(2), Tree(3)]), Tree(5, [Tree(3), Tree(4)])])
    >>> prune_small(t3, 2)
    >>> t3
    Tree(6, [Tree(1), Tree(3, [Tree(1), Tree(2)])])
    """
    #先处理当前节点
    while len(t.branches) > n:
        largest = max(t.branches, key= lambda b: b.label)
        t.branches.remove(largest)
    #再递归处理子数
    for b in t.branches:
        prune_small(b,n)



def prune_small(t, n):
    while len(t.branches) > n:
        largest = max(t.branches, key = lambda b : b.label) #要取的是值在通过函数之后的值
        t.branches.remove(largest)
    for b in t.branches:
        prune_small(b,n)






class Link:
    """A linked list.

    >>> s = Link(1)
    >>> s.first
    1
    >>> s.rest is Link.empty
    True
    >>> s = Link(2, Link(3, Link(4)))
    >>> s.first = 5
    >>> s.rest.first = 6
    >>> s.rest.rest = Link.empty
    >>> s                                    # Displays the contents of repr(s)
    Link(5, Link(6))
    >>> s.rest = Link(7, Link(Link(8, Link(9))))
    >>> s
    Link(5, Link(7, Link(Link(8, Link(9)))))
    >>> print(s)                             # Prints str(s)
    <5 7 <8 9>>
    """ 
class Link:
    empty = ()
    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest
    def __repr__(self):
        if self.rest is not Link.empty:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'
    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'


class Tree:
    """
    >>> t = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
    >>> t.label
    3
    >>> t.branches[0].label
    2
    >>> t.branches[1].is_leaf()
    True
    """
    def __init__(self, label, branches=[]):
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label
        self.branches = list(branches)

    def is_leaf(self):
        return not self.branches

    def map(self, fn):
        """
        Apply a function `fn` to each node in the tree and mutate the tree.

        >>> t1 = Tree(1)
        >>> t1.map(lambda x: x + 2)
        >>> t1.map(lambda x : x * 4)
        >>> t1.label
        12
        >>> t2 = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
        >>> t2.map(lambda x: x * x)
        >>> t2
        Tree(9, [Tree(4, [Tree(25)]), Tree(16)])
        """
        self.label = fn(self.label)
        for b in self.branches:
            b.map(fn)

    def __contains__(self, e):
        """
        Determine whether an element exists in the tree.

        >>> t1 = Tree(1)
        >>> 1 in t1
        True
        >>> 8 in t1
        False
        >>> t2 = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
        >>> 6 in t2
        False
        >>> 5 in t2
        True
        """
        if self.label == e:
            return True
        for b in self.branches:
            if e in b:
                return True
        return False

    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return 'Tree({0}{1})'.format(self.label, branch_str)

    def __str__(self):
        def print_tree(t, indent=0):
            tree_str = '  ' * indent + str(t.label) + "\n"
            for b in t.branches:
                tree_str += print_tree(b, indent + 1)
            return tree_str
        return print_tree(self).rstrip()

