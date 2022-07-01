class LRS_Suffix_Array:

    def get_suffix(self, s):
        suffix = []
        for i in range(0, len(s)):
            suffix.append(s[i:len(s)])
        return suffix
        
    def get_sorted_suffix(self, suffix):
        return sorted(suffix)      

    def get_suffix_array(self, suffix):
        return sorted(range(len(suffix)), key = suffix.__getitem__)

    def get_lcp_array(self, suffix_array, s):
        rank = [0 for i in range(0, len(suffix_array))]

        for i in range(0, len(rank)):
            rank[suffix_array[i]] = i

        lcp = [0 for i in range(0, len(suffix_array))]
        h = 0
        for i in range(0, len(suffix_array)):
            if rank[i] > 1:
                k = suffix_array[rank[i] - 1]
                while (i+h)<len(s) and (k+h)<len(s) and s[i+h] == s[k+h]:
                    h = h + 1
                lcp[rank[i]] = h
                if h > 0:
                    h = h - 1
        return lcp

    def get_lrs(self, lcp, sorted_suffix):
        idx = [i for i, j in enumerate(lcp) if j == max(lcp)]
        results = []
        for i in idx:
            results.append(sorted_suffix[i][0:lcp[i]])
        return results
    
    def run(self, s):
        if s[len(s) - 1] != '$':
            s += '$'
        suffix = self.get_suffix(s)
        print(suffix)
        sorted_suffix = self.get_sorted_suffix(suffix)
        print(sorted_suffix)
        suffix_array = self.get_suffix_array(suffix)
        print(suffix_array)
        lcp = self.get_lcp_array(suffix_array, s)
        print(lcp)
        lrs = self.get_lrs(lcp, sorted_suffix)
        return lrs
    
lrs_sa = LRS_Suffix_Array()
print(lrs_sa.run('ababbaabaa'))



#from Bio import SeqIO

#fasta = SeqIO.parse(open('sequence.fasta'), 'fasta')
#dna_str = ''
#for f in fasta:
#    dna_str += str(f.seq)
#lrs_sa = LRS_Suffix_Array()
#print(lrs_sa.run(dna_str))