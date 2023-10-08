public abstract class Item {
    protected String name;
    protected int sellIn;
    protected int quality;

    public Item(String name, int sellIn, int quality) {
        this.name = name;
        this.sellIn = sellIn;
        this.quality = quality;
    }

    public abstract void update();

    protected void decreaseSellIn() {
        sellIn--;
    }

    protected void increaseQuality() {
        if (quality < 50) {
            quality++;
        }
    }

    protected void decreaseQuality() {
        if (quality > 0) {
            quality--;
        }
    }
}

public class AgedBrie extends Item {

    public AgedBrie(int sellIn, int quality) {
        super("Aged Brie", sellIn, quality);
    }

    @Override
    public void update() {
        decreaseSellIn();
        increaseQuality();
    }
}

public class Sulfuras extends Item {

    public Sulfuras(int sellIn, int quality) {
        super("Sulfuras, Hand of Ragnaros", sellIn, quality);
    }

    @Override
    public void update() {
        // Sulfuras does not need to be updated
    }
}

public class BackstagePasses extends Item {

    public BackstagePasses(int sellIn, int quality) {
        super("Backstage passes to a TAFKAL80ETC concert", sellIn, quality);
    }

    @Override
    public void update() {
        decreaseSellIn();

        if (sellIn < 0) {
            quality = 0;
        } else if (sellIn < 5) {
            quality += 3;
        } else if (sellIn < 10) {
            quality += 2;
        } else {
            increaseQuality();
        }
    }
}

public class ConjuredItem extends Item {

    public ConjuredItem(String name, int sellIn, int quality) {
        super(name, sellIn, quality);
    }

    @Override
    public void update() {
        decreaseSellIn();
        decreaseQuality();
        decreaseQuality();
        if (sellIn < 0) {
            decreaseQuality();
            decreaseQuality();
        }
    }
}
