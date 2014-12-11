(ns easy-word-counting.core
  (:gen-class)
  (require [clojure.string :as str])
  (require [clojure.java.io :as io]))

;;(defn -main
;;  "Reads in source book text and counts the number of occurrences of each word in the text."
;;  [& args]
;;  ;; set file path, concatted strings return a vector of characters, so converting to string
;;  (def file-path (apply str (concat (System/getProperty "user.dir") "/resources/pg47498.txt")))
;;  (def text-lines (with-open [book-text (io/reader file-path)] (line-seq book-text)))
;;  (defn get-line-words [line] (str/split line #" "))
;;  (defn strip-punc [word] (apply str (remove #((set '(\. \; \: \, \( \) \' \+ \- \|)) %) word)))
;;  (defn count-word [word word-map] (update-in word-map [word] (fnil inc 0)))
;;  (def word-counts {})
;;  (def words (map get-line-words text-lines))
;;  (defn dict-inc [m word] (update-in m [word] (fnil inc 0)))
  
;;  (println text-lines)
;;   (reduce dict-inc word-counts words)
;; )
	      ;; skip spaces, otherwise catalog word
	      ;;  (if (= word "") nil (strip-punc word) )
	      ;;)
;;	    )
;;  (println (take 10 words))

(defn -main
  "Reads in source book text and counts the number of occurrences of each word in the text."
  [& args]
  
  (defn strip-punc [word] (apply str (remove #((set '(\. \; \: \, \( \) \' \+ \- \|)) %) word)))
  (defn get-line-words [line] (re-seq #"\w+" (str/trim line)))
  (defn dict-inc [m word] (update-in m [word] (fnil inc 0)))
  
  (def file-path (apply str (concat (System/getProperty "user.dir") "/resources/pg47498.txt")))
  (def text-lines (with-open [book-text (io/reader file-path)] (doall (line-seq book-text))))

  (println
    (reduce dict-inc {}
      (map strip-punc 
        (map get-line-words ["This is one sentence." "This is another snetence."])
      )
    )
  )
)