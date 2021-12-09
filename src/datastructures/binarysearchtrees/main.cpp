#include <gtest/gtest.h>

#include <iostream>

#include "binarysearchtrees.hpp"

// TEST(HashChaining, TestInitialisation) {
//    auto hashmap_empty = HashChaining<std::string, std::string>();
//    EXPECT_EQ(hashmap_empty.Count(), 0);
//    auto hashmap = HashChaining<std::string, std::string>("AAA", "Value123");
//    EXPECT_EQ(hashmap.Count(), 1);
//}

int main(int argc, char *argv[]) {
  auto tree = BinarySearchTree<std::string, std::string>();

  //    testing::InitGoogleTest(&argc, argv);
  //    return RUN_ALL_TESTS();
};