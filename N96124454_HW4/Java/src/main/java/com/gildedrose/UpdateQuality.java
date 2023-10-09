package com.gildedrose;

public interface UpdateQuality {
    void update(Item item);
}

public class AgedBrieUpdate implements UpdateQuality {
    @Override 
    public void update(Item item) {
        decreaseSellIn(item);
        increaseQuality(item);
    } 
}

public class SulfurasUpdate implements UpdateQuality {
    @Override
    public void update(Item item) {
        // Sulfuras does not need to be updated
    }
}

public class BackstagePassesUpdate implements UpdateQuality {
    @Override
    public void update(Item item) {
        decreaseSellIn(item);

        if (item.sellIn < 0) {
            item.quality = 0;
        } else if (item.sellIn < 5) {
            item.quality += 3;
        } else if (item.sellIn < 10) {
            item.quality += 2;
        } else {
            increaseQuality(item);
        }
    }
}

public class ConjuredUpdate implements UpdateQuality {
    @Override
    public void update(Item item){
        decreaseSellIn(item);
        decreaseQuality(item);
        decreaseQuality(item);
        if (item.sellIn < 0) {
            decreaseQuality(item);
            decreaseQuality(item);
        }
    }
}