package edu.msudenver.venue;

import com.fasterxml.jackson.annotation.JsonProperty;
import edu.msudenver.city.City;
import edu.msudenver.constraints.EnumNamePattern;

import javax.persistence.*;
import javax.validation.constraints.NotNull;

@Entity
@Table(name = "venues")
public class Venue {
    @Id
    @Column(name = "venue_id", columnDefinition = "SERIAL")
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @JsonProperty(access = JsonProperty.Access.READ_ONLY)
    private Long venueId;

    @Column(name = "country_code")
    @JsonProperty(access = JsonProperty.Access.WRITE_ONLY)
    @NotNull(message = "countryCode cannot be null")
    private String countryCode;

    @Column(name = "postal_code")
    @JsonProperty(access = JsonProperty.Access.WRITE_ONLY)
    @NotNull(message = "postalCode cannot be null")
    private String postalCode;

    @ManyToOne()
    @JoinColumns({
        @JoinColumn(name = "country_code", referencedColumnName = "country_code", insertable = false, updatable = false),
        @JoinColumn(name = "postal_code", referencedColumnName = "postal_code", insertable = false, updatable = false)
    })
    @JsonProperty(access = JsonProperty.Access.READ_ONLY)
    private City city;

    @Column(name = "name")
    @NotNull(message = "name cannot be null")
    private String name;

    @Column(name = "street_address")
    private String streetAddress;

    @Column(name = "type")
    @EnumNamePattern(regexp = "private|public")
    private String type;

    @Column(name = "active")
    private Boolean active = true;

    public Venue() {
    }

    public Venue(Long venueId, String countryCode, String postalCode, String name, String streetAddress, String type, Boolean active) {
        this.venueId = venueId;
        this.countryCode = countryCode;
        this.postalCode = postalCode;
        this.name = name;
        this.streetAddress = streetAddress;
        this.type = type;
        this.active = active;
    }

    public Long getVenueId() {
        return venueId;
    }

    public void setVenueId(Long venueId) {
        this.venueId = venueId;
    }

    public City getCity() {
        return city;
    }

    public void setCity(City city) {
        this.city = city;
    }

    public String getCountryCode() {
        return countryCode;
    }

    public void setCountryCode(String countryCode) {
        this.countryCode = countryCode;
    }

    public String getPostalCode() {
        return postalCode;
    }

    public void setPostalCode(String postalCode) {
        this.postalCode = postalCode;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getStreetAddress() {
        return streetAddress;
    }

    public void setStreetAddress(String streetAddress) {
        this.streetAddress = streetAddress;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public Boolean getActive() {
        return active;
    }

    public void setActive(Boolean active) {
        this.active = active;
    }
}
