package example;

/* metamodel_version: 1.12.0 */
/* version: 2.2.4 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  What a product's vendor has said about a vulnerability.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class NvdVendorComment  {

  private ZonedDateTime lastModified;
  private String organization;
  private String comment;


}