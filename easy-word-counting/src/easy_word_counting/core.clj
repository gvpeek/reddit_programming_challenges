(ns easy-word-counting.core
  (:gen-class)
  (require [clojure.string :as str])
  (require [clojure.java.io :as io]))

(defn -main
  "Reads in source book text and counts the number of occurrences of each word in the text."
  [& args]
  ;; set file path, concatted strings return a vector of characters, so converting to string
  (def file-path (apply str (concat (System/getProperty "user.dir") "/resources/pg47498.txt")))
  (defn strip-punc [word] (str (remove #((set (\. \; \: \,)) %) word)))
  ;; open file
  (with-open [book-text (io/reader file-path)]
  ;; read each line
    (doseq [line (line-seq book-text)]
      ;; split the line on spaces
      (doseq [word (str/split line #" ")]
      ;; skip spaces, otherwise catalog word
        (if (= word "") nil (println #((strip-punc word))))
      )
    )
  )
)
