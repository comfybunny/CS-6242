package edu.gatech.cse6242

import org.apache.spark.SparkContext
import org.apache.spark.SparkContext._
import org.apache.spark.SparkConf

object Task2 {
  def main(args: Array[String]) {
    val sc = new SparkContext(new SparkConf().setAppName("Task2"))

    // read the file
    val file = sc.textFile("hdfs://localhost:8020" + args(0))

    val tokenized = file.flatMap(_.split("\n"))
    /* TODO: Needs to be implemented */
    val secondPass = tokenized.map(_.split("\t"))
    // secondPass.foreach(println)
    val incomingEdge = secondPass.map(x=> x(1)->x(2).toInt).reduceByKey(_ + _).sortByKey().map{ case (key, value) => Array(key, value).mkString("\t") }
    // store output on given HDFS path.
    // YOU NEED TO CHANGE THIS
    incomingEdge.saveAsTextFile("hdfs://localhost:8020" + args(1))
  }
}
