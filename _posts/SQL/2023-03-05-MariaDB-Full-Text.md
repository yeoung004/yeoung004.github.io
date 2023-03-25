# Using Full-Text Search in MariaDB

Full-text search is a powerful feature that allows you to search for words or phrases within text fields in your database. It is particularly useful for applications that involve searching large amounts of text data, such as blog posts or product descriptions. In this post, we'll explore how to use full-text search in MariaDB.

### Setting Up Full-Text Search

Before we can start using full-text search, we need to make sure that our tables are set up properly. To enable full-text search in MariaDB, we need to create a full-text index on one or more columns that contain the text we want to search. Here's an example:

```
CREATE TABLE products (
  id INT NOT NULL PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  FULLTEXT (name, description)
);
```

In this example, we've created a **_`products`_** table with a full-text index on the name and description columns. This will allow us to search for **_`products`_** based on their **_`name`_** or description.

### Performing a Full-Text Search

Once our table is set up with a full-text index, we can perform a full-text search using the **_`MATCH() AGAINST()`_** syntax. Here's an example:

`SELECT * FROM products WHERE MATCH(name, description) AGAINST('organic coffee');`

In this example, we're searching for products that contain the words "organic" and "coffee" in either the **_`name`_** or **_`description`_** column. Note that we don't need to use the **_`%`_** wildcard like we would with a **_`LIKE`_** query.

### Using Boolean Operators

Full-text search also supports Boolean operators such as **_`AND`_** , **_`OR`_** , and **_`NOT`_** . Here's an example:

`SELECT * FROM products WHERE MATCH(name, description) AGAINST('+organic +coffee -decaf' IN BOOLEAN MODE);`
In this example, we're searching for products that contain the words "organic" and "coffee", but not "decaf". The + and - symbols indicate that a word is required or prohibited, respectively.

### Using Natural Language Mode

By default, full-text search in MariaDB uses a "natural language" mode that takes into account factors such as word proximity and term frequency. However, if you want to perform a more precise search, you can use the "Boolean" mode instead. Here's an example:

`SELECT * FROM products WHERE MATCH(name, description) AGAINST('+"organic coffee"' IN BOOLEAN MODE);`
In this example, we're searching for products that contain the phrase "organic coffee", with the words in that order.

### Stop word

In full text search, a stop word is a common word that is ignored during the indexing and searching process because it is deemed to have little value in discriminating between different documents or records.

Stop words are typically short, commonly occurring words like "the," "and," "a," "in," etc. that appear frequently in a language but are not very useful in helping to distinguish between different documents or records. By ignoring these words, the full text search algorithm can focus on the more important keywords and phrases that are more relevant to the user's search query.

Most full text search engines provide a built-in list of stop words for the supported languages, but users can also customize the stop word list to suit their specific needs. It is important to note that excluding stop words from the index can improve search performance and reduce the size of the index, but it can also lead to false negatives if a search query includes a stop word that is actually part of a relevant phrase or term. Therefore, it is important to carefully evaluate the impact of removing stop words on the search quality and relevance of the results.

`SELECT * FROM information_schema.INNODB_FT_DEFAULT_STOPWORD;`
This will show the default stop words used by InnoDB full-text search. You can also add or remove stop words from this table if you want to customize the stop words list. Keep in mind that you need the SUPER privilege to modify the stop words list.
![stopword](https://raw.githubusercontent.com/yeoung004/yeoung004.github.io/main/_posts/SQL/stopword.png)

### Token size

In full text search, the term "token size" refers to the number of characters or words that are indexed as a single searchable unit. The token size determines how finely the full text search engine breaks down the text into separate units for indexing and searching.

For example, if the token size is set to 1, each individual character in the text will be indexed and searchable. If the token size is set to 2, every two consecutive characters will be indexed and searchable as a single unit. If the token size is set to a larger number such as 3, 4, or 5, consecutive words or phrases of that length will be indexed and searchable as single units.

Choosing the appropriate token size depends on the type of data being indexed and the specific requirements of the search. For example, a smaller token size might be appropriate for searching small snippets of text, such as product names or short descriptions, while a larger token size might be more appropriate for searching longer documents, such as articles or books.

#### Amazon RDS for MariaDB involves modifying the parameter group

You can optimize your db token size. If token size close by 1, It makes your db server is slow cause You db server searches every 1 size token when user searches. so keep in mind that.

this is how to change token size in AWS rds:

1. Go to the RDS dashboard in the AWS Management Console and select your database instance and Parameter groups.
2. Click "Create parameter group" (You can't modify default parameter group).
   ![rds1](https://raw.githubusercontent.com/yeoung004/yeoung004.github.io/main/_posts/SQL/rds1.png)
3. Write name of parameter group and click create button.
   ![rds2](https://raw.githubusercontent.com/yeoung004/yeoung004.github.io/main/_posts/SQL/rds2.png)
4. Click on it to open the parameter group configuration page.
   On the parameter group configuration page, search for the innodb_ft_min_token_size parameter and modify its value to your desired ft_min_word_length (in bytes). Note that the innodb_ft_max_token_size parameter can also be modified to set the maximum length of indexed words.
   ![rds5](https://raw.githubusercontent.com/yeoung004/yeoung004.github.io/main/_posts/SQL/rds5.png)
5. Finally, go back to the RDS dashboard and select your database instance again. Under the "Instance actions" menu, select "Modify" and select the updated parameter group from the "DB parameter group" dropdown. Follow the prompts to apply the changes to your database instance.
   ![rds3](https://raw.githubusercontent.com/yeoung004/yeoung004.github.io/main/_posts/SQL/rds3.png)
   ![rds4](https://raw.githubusercontent.com/yeoung004/yeoung004.github.io/main/_posts/SQL/rds4.png)

### Conclusion

Full-text search is a powerful feature that can help you build more sophisticated search functionality into your applications. By creating full-text indexes on your tables and using the MATCH() AGAINST() syntax, you can quickly and efficiently search through large amounts of text data in your database.
