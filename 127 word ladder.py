class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        curlist = [beginWord]
        wordListSet = set(wordList)
        wlen = len(beginWord)
        level = 1
        while curlist:
            nextlist = []
            for word in curlist:
                # get neighbor word list and and delete them from wordlist
                # iterate all characters of the word and replace it with a-z
                for i in range(wlen):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        rWord = word[:i] + c + word[i+1:]
                        if rWord in wordListSet:
                            if rWord == endWord:
                                return level + 1
                            nextlist.append(rWord)
                            wordListSet.remove(rWord)
            if nextlist:
                level += 1
            curlist = nextlist
        return 0    

print(Solution().ladderLength("hit","cog",["hot","dot","dog","lot","log"]))