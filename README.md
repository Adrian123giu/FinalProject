# Final Project - API Testing Framework

This repository contains an automated API testing framework for the JSONPlaceholder API, a simple mock API that provides information on posts, comments, todos, and users.

## Application Details Tested

**Purpose:**
Simulates a straightforward API to deliver information about posts, comments, tasks, and users.

**Data Source:**
The data is simulated and returned from https://jsonplaceholder.typicode.com.

## Application Structure

### Requests

Multiple request classes have been created, each with specific methods for interacting with the different endpoints of the JSONPlaceholder API.

#### PostsRequest
- Methods to retrieve all posts and a specific post by ID, as well as to create a new post.

#### CommentsRequest
- Methods to retrieve all comments and specific comments for a post by post ID.

#### TodosRequest
- Methods to retrieve all todos and a specific todo by ID.

#### UsersRequest
- Methods to retrieve all users and a specific user by ID.

#### GeneralRequests
- Methods for general requests, such as accessing a non-existent endpoint and checking the response time for a valid endpoint.

### Tests

Corresponding tests have been created for each set of requests to verify the functionality and performance of the API.

#### Tests for PostsRequest
- Tests to retrieve all posts, create a post, and get a specific post.

#### Tests for CommentsRequest
- Tests to retrieve all comments and comments filtered by post ID.

#### Tests for TodosRequest
- Tests to retrieve all todos and a specific todo.

#### Tests for UsersRequest
- Tests to retrieve all users and a specific user.

#### General Tests (TestGeneral)
- Test to verify the response to a request to a non-existent endpoint and test to check the response time for a valid endpoint.
