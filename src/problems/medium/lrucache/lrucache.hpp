#include <list>
#include <unordered_map>
#include <stdexcept>

template <typename Key,typename  Value> class LRUCache {
// Store pair of key, values. We need to store the keys, for O(1) delete of last element
std::list<std::pair<Key, Value > > dq;
// Store references of iterators in map
std::unordered_map<Key, typename std::list<std::pair<Key, Value > >::iterator> map;
// Maximum capacity of list
std::size_t max_capacity;

public:
    // Function should not throw
    LRUCache<Key,Value>(std::size_t max_capacity) noexcept : dq({}), map({}), max_capacity(max_capacity){};
    typename std::list<std::pair<Key, Value > >::const_iterator get(Key);
    void put(Key, Value);
    typename std::list<std::pair<Key, Value > >::const_iterator cbegin() { return dq.cbegin(); }
    typename std::list<std::pair<Key, Value > >::const_iterator cend() { return dq.cend(); }
    std::size_t capacity() {return max_capacity;}
    std::size_t size() {return dq.size();}
    void print();

};

template <typename Key,typename  Value> void LRUCache<Key, Value>::put(Key key, Value value){
    // Search for key
    if (map.find(key) != map.end()){
      // If key exists, move it to front of list
        dq.splice(dq.cbegin(),dq,map[key]);
        // Update its value
        dq.begin()->second = value;
        // Update iterator pointer to begin
        map[key] = dq.begin();
    }
      // Insert new k,v
    else{
    // If addition exceed capacity
    // remove element from end of que
    if (dq.size() >= max_capacity){
      // Get pair at end
        auto back = dq.back();
        // Extract key from end pair
        auto end_key = std::get<0>(back);
        // remove it from the map
        map.erase(end_key);
        // remove it from the end of the list
        dq.pop_back();
    }

    dq.push_front(std::make_pair(key, value));
    map[key] = dq.begin();
    }
}

template <typename Key,typename Value> typename
    std::list<std::pair<Key, Value > >::const_iterator  LRUCache<Key, Value>::get(Key key){
    // Either return iterator to found element or to end of list
    // NOTE: a better design pattern would be to return a const iterator to the value
    // and on not found, return a const iterator to end
    // This would require writing a custom iterator class which would go through
    // std::list<std::pair<Key, Value > >
    // but only return the value part of the pair
    if (map.find(key) != map.end()){
      // If key exists, move it to front of list
      dq.splice(dq.cbegin(),dq,map[key]);
      // Update k,iterator map to point to begin
      map[key] = dq.begin();
      return dq.cbegin();
    }
    return dq.cend();
}

template <typename Key,typename  Value> void LRUCache<Key, Value>::print(){
  auto pCrawler = dq.cbegin();
  while (pCrawler != dq.cend()){
    std::cout << "(" << std::get<0>(*pCrawler) << "," << std::get<1>(*pCrawler) << "), ";
    pCrawler++;
  }
}