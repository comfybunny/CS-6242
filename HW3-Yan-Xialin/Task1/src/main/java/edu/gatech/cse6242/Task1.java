package edu.gatech.cse6242;

import org.apache.hadoop.fs.Path;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.io.*;
import org.apache.hadoop.mapreduce.*;
import org.apache.hadoop.util.*;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

import java.io.IOException;
import java.util.StringTokenizer;

// GOAL: calculate the sum of the weights of all incoming edges for each node in the graph
public class Task1 {

	public static class TokenizerMapper extends Mapper<Object, Text, Text, IntWritable>{
		private Text incoming = new Text();
		private IntWritable output_weight = new IntWritable();
		public void map(Object key, Text value, Context context) throws IOException, InterruptedException{

			

			StringTokenizer itr = new StringTokenizer(value.toString());
			// The Mapper implementation processes one line at a time as provided by the specified TextInputFromat
			// The StringTokenizer splits the line into tokens separated by whitespaces
			
			String src = itr.nextToken();
			String tgt = itr.nextToken();
			String weight = itr.nextToken();
			incoming.set(tgt);
			output_weight.set(Integer.parseInt(weight));
			context.write(incoming, output_weight);
		}
	}

	public static class IntSumReducer extends Reducer<Text, IntWritable, Text, IntWritable>{
		private IntWritable result = new IntWritable();
		public void reduce(Text key, Iterable<IntWritable> values, Context context) throws IOException, InterruptedException{
			int sum = 0;
			for(IntWritable val: values){
				sum += val.get();
			}
			result.set(sum);
			context.write(key, result);
		}
	}

	public static void main(String[] args) throws Exception {
	Configuration conf = new Configuration();
	Job job = Job.getInstance(conf, "Task1");

	/* TODO: Needs to be implemented */
	job.setJarByClass(Task1.class);
	job.setMapperClass(TokenizerMapper.class);
	job.setCombinerClass(IntSumReducer.class);
    job.setReducerClass(IntSumReducer.class);
    job.setOutputKeyClass(Text.class);
    job.setOutputValueClass(IntWritable.class);

	FileInputFormat.addInputPath(job, new Path(args[0]));
	FileOutputFormat.setOutputPath(job, new Path(args[1]));
	System.exit(job.waitForCompletion(true) ? 0 : 1);
	}
}
