import os
import re
import heapq

from collections import defaultdict

execution_dir = os.path.dirname(os.path.realpath(__file__))
file_path = os.path.join(execution_dir, 'holy_grail.txt')

speaker = re.compile(r'.*:')

stage_directions = 0
scene = 0
total_words = 0
words_per_scene = 0
scene_words = defaultdict(int)
with open(file_path, 'r+') as script:
    for line in script:
        # print line
        scene_nbr = re.match('^Scene (\d+)', line)
        if scene_nbr:
            if scene:
                print
                print 'Scene', scene, words_per_scene
                word_list = []
                for word, count in scene_words.iteritems():
                    heapq.heappush(word_list, (count, word))
                for count, top_word in heapq.nlargest(3, word_list):
                    pct = count / float(words_per_scene)
                    print 'Word: {0} \t Count: {1} \t Pct: {2:.2%}'.format(top_word, count, pct)
            words_per_scene = 0
            scene_words = defaultdict(int)
            scene = scene_nbr.group(1)
        if '[' in line and ']' in line:
            stage_directions += 1
        else:
            words = line.split()
            if words:
                if speaker.match(words[0]):
                    del words[0]
            total_words += len(words)
            words_per_scene += len(words)
            for word in words:
                scene_words[word] += 1
            

    print stage_directions