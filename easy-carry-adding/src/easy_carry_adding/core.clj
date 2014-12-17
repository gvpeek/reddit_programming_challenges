(ns easy-carry-adding.core
  (:gen-class)
  (require [clojure.string :as str])
  (require [clojure.math.numeric-tower :as math]))

(defn -main
  "Take input of the format '3+4+5' and present the solution in 'carry adding' format"
  [& args]

  (defn str2int [str] (Integer. str))
  ;; map creates a list, but we need a vector to do the padding
  (defn reverse-vector [str] (into [] (map #(Character/getNumericValue %) (str/reverse str))))
  (defn pad-vector [len vec] (concat vec (into [] (repeat (- (- len 1) (count vec)) 0))))
  (defn get-carry-digit [vec] (int (math/floor (/ (reduce + vec) 10))))
  
  ;; input comes in as ArraySeq. Split into strings on '+' character
  (def integer-strings (str/split (first args) #"\+"))
  (def reverse-int-strings (map reverse-vector integer-strings))
  (def sum (reduce + (map str2int integer-strings)))
  (def sum-length (count (str sum)))
  ;; adding zeros to the vectorized input, otherwise the slicing stops at the length of the shortest input
  (def padded-input-vectors (map pad-vector (repeat (count reverse-int-strings) sum-length) reverse-int-strings))
  (def carry-vectors (apply map vector padded-input-vectors))
  ;; right-justify format
  (def formatter (str/join ["%" (str sum-length) "d"]))
  (def dividing-line (str/join (repeat sum-length "-")))
  
  (doseq [x integer-strings] (println (format formatter (str2int x))))
  (println dividing-line)
  (println sum)
  (println dividing-line)
  (println (str/replace (str/join (reverse (map get-carry-digit carry-vectors))) "0" " "))
)
