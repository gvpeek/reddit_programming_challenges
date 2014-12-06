(ns easy-word-counting.core
  (:gen-class)
  (require [clojure.java.io :as io]))

(defn -main
  "I don't do a whole lot ... yet."
  [& args]
  (def file-path (clojure.string/join (concat (System/getProperty "user.dir") "/resources/pg47498.txt")))
  (with-open [book-text (io/reader file-path)]
    (doseq [line (line-seq book-text)]
      (println line))))
