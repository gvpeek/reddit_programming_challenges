(ns easy-word-counting.core
  (:gen-class)
  (require [clojure.string :as str])
  (require [clojure.java.io :as io]))

(defn -main
  "I don't do a whole lot ... yet."
  [& args]
  ;; set file path, concatted strings have spaces in between, so they must be joined after
  (def file-path (clojure.string/join (concat (System/getProperty "user.dir") "/resources/pg47498.txt")))
  ;; open file
  (with-open [book-text (io/reader file-path)]
  ;; read each line
    (doseq [line (line-seq book-text)]
      ;; split the line on spaces
      (doseq [word (str/split line #" ")]
      ;; skip spaces, otherwise catalog word
        (if (= word "") nil (println word))))))
