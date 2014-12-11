(ns easy-word-counting.core
  (:gen-class)
  (require [clojure.string :as str])
  (require [clojure.java.io :as io]))

(defn -main
  "Reads in source book text and counts the number of occurrences of each word in the text."
  [& args]
  
  (def file-path (apply str (concat (System/getProperty "user.dir") "/resources/pg47498.txt")))
  ;; line-seq creates a lazy sequence, so we need to add a doall to realize it
  (def text-lines (with-open [book-text (io/reader file-path)] (doall (line-seq book-text))))

  ;; remove produces a vector of characters, so need to turn them back into strings
  (defn strip-punc [word] (apply str (remove #((set '(\. \; \: \, \( \) \' \+ \- \| \_)) %) word)))
  (defn get-line-words [word-list line] (into word-list (re-seq #"\w+" (str/trim line))))
  ;; lifted dict-inc from https://blog.safaribooksonline.com/2013/08/14/clojure-thinking-in-hashmaps/ 
  ;; didn't intend to use someone elses solution, but after stubling upon an elegant one
  ;; it was hard to put it out of my mind to do it diffently (and likely worse)
  ;; From the page... fnil is a function, which creates a function that will use a default value when passed nil
  (defn dict-inc [word-counts word] (update-in word-counts [word] (fnil inc 0)))
  
  (println
    (reduce dict-inc {}
      (map strip-punc 
        (reduce get-line-words [] text-lines)
      )
    )
  )
)