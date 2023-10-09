package com.gildedrose;

public class UpdateUtils {
    private static final int MAX_QUALITY = 50;
    private static final int MIN_QUALITY = 0;

    public void decreaseSellIn(Item item) {
        item.sellIn--;
    }

    public void increaseQuality(Item item) {
        if (item.quality < MAX_QUALITY) {
            item.quality++;
        }
    }

    public void decreaseQuality(Item item) {
        if (item.quality > MIN_QUALITY) {
            item.quality--;
        }
    }
}