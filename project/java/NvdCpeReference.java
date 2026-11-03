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
  A page about a product, and what kind of page it is.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class NvdCpeReference  {

  private String type;
  private String ref;


}