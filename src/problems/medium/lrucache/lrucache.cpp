#include <gtest/gtest.h>
#include "lrucache.hpp"

TEST(LRUCache, TestSimple) {

auto cache = LRUCache<std::string,std::string>(2);
EXPECT_EQ(2, cache.capacity());
EXPECT_EQ(0, cache.size());
cache.put("1","1");
cache.put("2","2");
EXPECT_EQ(2, cache.capacity());
EXPECT_EQ(2, cache.size());
EXPECT_EQ("2", cache.get("2")->second);
// expect movement of "1","1" to front
EXPECT_EQ("1", cache.get("1")->second);
//// Expect eviction of "2","2"
cache.put("3","3");
EXPECT_EQ(cache.cend(), cache.get("2"));
//// Expect eviction of "1","1"
cache.put("4","4");
EXPECT_EQ(cache.cend(), cache.get("1"));
EXPECT_EQ("3", cache.get("3")->second);
EXPECT_EQ("4", cache.get("4")->second);

}

int main(int argc, char *argv[]) {
    testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}